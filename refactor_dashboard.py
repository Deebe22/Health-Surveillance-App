import os

path = r'c:\Users\Deepi\health_surveillance_app\lib\screens\dashboard_screen.dart'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add _selectedIndex
if 'int _selectedIndex = 0;' not in text:
    target_class = 'class _DashboardScreenState extends State<DashboardScreen> {'
    text = text.replace(target_class, target_class + '\n  int _selectedIndex = 0;')

# 2. Update logic calculation
old_logic = """    int totalCases = 0;
    int activeHotspotsCount = 0;
    Map<String, _DiseaseBreakdown> diseaseBreakdown = {};

    try {
      final reports = AppData.globalReports;
      riskLevel = PredictionEngine.calculateRiskLevel(reports);
      predictedTrend = PredictionEngine.predictUpcomingRisk(reports);
      regionalAggregates = PredictionEngine.getRegionalAggregates(reports);
      
      totalCases = regionalAggregates.fold(0, (sum, a) => sum + a.totalCases);
      activeHotspotsCount = regionalAggregates.where((a) => a.riskLevel == 'HIGH' || a.riskLevel == 'MEDIUM').length;

      // Build disease-wise breakdown from globalReports
      diseaseBreakdown = _computeDiseaseBreakdown(reports);
    } catch (e) {"""

new_logic = """    int totalCases = 0;
    int totalReports = 0;
    int activeHotspotsCount = 0;
    Map<String, _DiseaseBreakdown> diseaseBreakdown = {};

    try {
      final reports = AppData.globalReports;
      totalReports = reports.length;
      riskLevel = PredictionEngine.calculateRiskLevel(reports);
      predictedTrend = PredictionEngine.predictUpcomingRisk(reports);
      regionalAggregates = PredictionEngine.getRegionalAggregates(reports);
      
      activeHotspotsCount = regionalAggregates.where((a) => a.riskLevel == 'HIGH' || a.riskLevel == 'MEDIUM').length;
      diseaseBreakdown = _computeDiseaseBreakdown(reports);
      
      int requestedCases = 0;
      if (diseaseBreakdown.containsKey('Fever')) requestedCases += diseaseBreakdown['Fever']!.totalCases;
      if (diseaseBreakdown.containsKey('Diarrhea')) requestedCases += diseaseBreakdown['Diarrhea']!.totalCases;
      if (diseaseBreakdown.containsKey('Stomach Pain')) requestedCases += diseaseBreakdown['Stomach Pain']!.totalCases;
      if (diseaseBreakdown.containsKey('Vomiting')) requestedCases += diseaseBreakdown['Vomiting']!.totalCases;
      totalCases = requestedCases;
    } catch (e) {"""

text = text.replace(old_logic, new_logic)

# 3. Replace body with IndexedStack or conditional build + bottomNavigationBar
old_body_start = """      body: Container(
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E3C72), Color(0xFF2A5298)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: SingleChildScrollView(
          child: Column(
            children: ["""

new_body_start = """      body: Container(
        height: double.infinity,
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Color(0xFF1E3C72), Color(0xFF2A5298)],
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
          ),
        ),
        child: _selectedIndex == 0 
            ? _buildHomeTab(context, l10n, localizedName, localizedRole, isAuthority, isPublic, totalCases, activeHotspotsCount, predictedTrend, riskLevel, diseaseBreakdown, regionalAggregates, totalReports)
            : _buildMenuTab(context, l10n, isPublic),
      ),
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: const Color(0xFF1E3C72),
        selectedItemColor: Colors.cyanAccent,
        unselectedItemColor: Colors.white54,
        currentIndex: _selectedIndex,
        onTap: (index) => setState(() => _selectedIndex = index),
        items: [
          BottomNavigationBarItem(icon: const Icon(Icons.dashboard), label: l10n.homeTab ?? 'Home'),
          BottomNavigationBarItem(icon: const Icon(Icons.grid_view), label: l10n.menuTab ?? 'Menu'),
        ]
      ),
    );
  }

  Widget _buildHomeTab(BuildContext context, dynamic l10n, String localizedName, String localizedRole, bool isAuthority, bool isPublic, int totalCases, int activeHotspotsCount, String predictedTrend, String riskLevel, Map<String, _DiseaseBreakdown> diseaseBreakdown, List<RegionalSummary> regionalAggregates, int totalReports) {
    return SingleChildScrollView(
      child: Column(
        children: ["""

text = text.replace(old_body_start, new_body_start)

# 4. We need to close _buildHomeTab, open _buildMenuTab where appropriate
old_summary_stats = """              // 📊 Summary Statistics
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Row(
                  children: [
                    _buildStatCard(l10n.totalCases, totalCases.toString(), Icons.people, Colors.blue),
                    const SizedBox(width: 10),
                    _buildStatCard(l10n.activeHotspots, activeHotspotsCount.toString(), Icons.location_on, Colors.red),
                    const SizedBox(width: 10),
                    _buildStatCard(l10n.aiTrendTitle, _localizeTrend(l10n, predictedTrend), Icons.trending_up, predictedTrend.contains('OUTBREAK') ? Colors.purple : Colors.teal),
                  ],
                ),
              ),"""

new_summary_stats = """              // 📊 Summary Statistics
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Column(
                  children: [
                    Row(
                      children: [
                        _buildStatCard(l10n.totalCases, totalCases.toString(), Icons.people, Colors.blue),
                        const SizedBox(width: 10),
                        _buildStatCard(l10n.activeHotspots, activeHotspotsCount.toString(), Icons.location_on, Colors.red),
                      ]
                    ),
                    const SizedBox(height: 10),
                    Row(
                      children: [
                        _buildStatCard(l10n.aiTrendTitle, _localizeTrend(l10n, predictedTrend), Icons.trending_up, predictedTrend.contains('OUTBREAK') ? Colors.purple : Colors.teal),
                        const SizedBox(width: 10),
                        _buildStatCard(l10n.totalReports ?? "Total Reports", totalReports.toString(), Icons.insert_chart, Colors.orange),
                      ]
                    )
                  ]
                ),
              ),"""

text = text.replace(old_summary_stats, new_summary_stats)

old_split_point = """              // 🏠 Public-Only: Daily Tip
              if (isPublic) ...["""

new_split_point = """        ],
      ),
    );
  }

  Widget _buildMenuTab(BuildContext context, dynamic l10n, bool isPublic) {
    return SingleChildScrollView(
      child: Column(
        children: [
              // 🏠 Public-Only: Daily Tip
              if (isPublic) ...["""

text = text.replace(old_split_point, new_split_point)

# 5. Remove the closing braces for original build() which were after GridView
old_closing = """              const SizedBox(height: 40),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildStatCard"""

new_closing = """              const SizedBox(height: 40),
            ],
          ),
    );
  }

  Widget _buildStatCard"""

text = text.replace(old_closing, new_closing)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Dashboard split completed successfully.")
