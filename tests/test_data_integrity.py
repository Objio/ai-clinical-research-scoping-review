# -*- coding: utf-8 -*-
"""
TDD Tests for PhD Thesis Data Verification
AI in Clinical Research Scoping Review
"""

import pytest

# Data from manuscript (verified)
CLUSTER_DATA = {
    'names': [
        'General ML/DL', 'AI in Clinical Care', 'ML Classification Systems',
        'Clinical Studies (Retrospective)', 'Healthcare Security & Federated',
        'Cardiovascular Risk', 'EHR Analytics', 'NLP & LLMs', 'Cancer Genomics',
        'MRI Imaging', 'Deep Neural Networks', 'Medical Image Segmentation',
        'CT Radiomics', 'Drug Discovery', 'Breast Cancer Imaging'
    ],
    'n': [1332, 903, 698, 691, 644, 549, 481, 458, 457, 447, 439, 424, 381, 278, 213],
    'pct': [15.9, 10.8, 8.3, 8.2, 7.7, 6.5, 5.7, 5.5, 5.4, 5.3, 5.2, 5.1, 4.5, 3.3, 2.5],
    'y2023': [322, 207, 150, 105, 129, 112, 102, 70, 107, 99, 83, 115, 56, 61, 51],
    'y2025': [543, 418, 276, 341, 301, 255, 207, 238, 198, 187, 192, 180, 184, 115, 89],
    'growth': [69, 102, 84, 225, 133, 128, 103, 240, 85, 89, 131, 57, 229, 89, 75]
}

EXPECTED_TOTAL = 8395


class TestDataIntegrity:
    """Tests for data integrity verification."""
    
    def test_total_documents(self):
        """Total documents should equal 8,395."""
        assert sum(CLUSTER_DATA['n']) == EXPECTED_TOTAL
    
    def test_cluster_count(self):
        """Should have exactly 15 clusters."""
        assert len(CLUSTER_DATA['names']) == 15
    
    def test_data_arrays_same_length(self):
        """All data arrays should have same length."""
        expected_len = len(CLUSTER_DATA['names'])
        assert len(CLUSTER_DATA['n']) == expected_len
        assert len(CLUSTER_DATA['pct']) == expected_len
        assert len(CLUSTER_DATA['y2023']) == expected_len
        assert len(CLUSTER_DATA['y2025']) == expected_len
        assert len(CLUSTER_DATA['growth']) == expected_len


class TestPercentages:
    """Tests for percentage calculations."""
    
    def test_percentages_sum_to_100(self):
        """Percentages should sum to approximately 100%."""
        total_pct = sum(CLUSTER_DATA['pct'])
        assert 99.0 <= total_pct <= 101.0, f"Sum is {total_pct}%"
    
    def test_percentages_match_n(self):
        """Each percentage should match N/Total."""
        total = sum(CLUSTER_DATA['n'])
        for i, name in enumerate(CLUSTER_DATA['names']):
            calculated = CLUSTER_DATA['n'][i] / total * 100
            actual = CLUSTER_DATA['pct'][i]
            assert abs(calculated - actual) < 0.5, f"{name}: calc={calculated:.1f}%, actual={actual}%"


class TestGrowthCalculations:
    """Tests for growth rate calculations."""
    
    def test_growth_formula(self):
        """Growth should be (y2025-y2023)/y2023 * 100."""
        for i, name in enumerate(CLUSTER_DATA['names']):
            y23 = CLUSTER_DATA['y2023'][i]
            y25 = CLUSTER_DATA['y2025'][i]
            calculated = (y25 - y23) / y23 * 100
            actual = CLUSTER_DATA['growth'][i]
            # Allow 5% tolerance for rounding
            assert abs(calculated - actual) < 5, f"{name}: calc={calculated:.0f}%, actual={actual}%"
    
    def test_top_growth_clusters(self):
        """NLP & LLMs should have highest growth (+240%)."""
        max_growth_idx = CLUSTER_DATA['growth'].index(max(CLUSTER_DATA['growth']))
        assert CLUSTER_DATA['names'][max_growth_idx] == 'NLP & LLMs'
        assert CLUSTER_DATA['growth'][max_growth_idx] == 240
    
    def test_second_highest_growth(self):
        """CT Radiomics should have second highest growth (+229%)."""
        sorted_growth = sorted(enumerate(CLUSTER_DATA['growth']), key=lambda x: -x[1])
        second_idx = sorted_growth[1][0]
        assert CLUSTER_DATA['names'][second_idx] == 'CT Radiomics'
        assert CLUSTER_DATA['growth'][second_idx] == 229


class TestTemporalConsistency:
    """Tests for temporal data consistency."""
    
    def test_y2025_greater_than_y2023(self):
        """All clusters should show growth (y2025 > y2023)."""
        for i, name in enumerate(CLUSTER_DATA['names']):
            assert CLUSTER_DATA['y2025'][i] > CLUSTER_DATA['y2023'][i], \
                f"{name} shows decline"
    
    def test_no_negative_values(self):
        """No negative values in any field."""
        for key in ['n', 'pct', 'y2023', 'y2025', 'growth']:
            assert all(v >= 0 for v in CLUSTER_DATA[key]), f"Negative value in {key}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
