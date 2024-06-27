import re
from youtube_dl.extractor.common import InfoExtractor
from youtube_dl.utils import ExtractorError, dict_get
import json
import coverage

branch_coverage_1 = {i: False for i in range(1300, 1400)}

def extract_selected_tab_wrapper(tabs):
    for tab in tabs:
        renderer = dict_get(tab, ('tabRenderer', 'expandableTabRenderer')) or {}
        if renderer.get('selected') is True:  # Branch ID 1300
            branch_coverage_1[1300] = True
            return renderer
    else:  # Branch ID 1301
        branch_coverage_1[1301] = True
        raise ExtractorError('Unable to find selected tab')

# Initialize coverage
cov = coverage.Coverage()
cov.start()

# Example test case
tabs = [{"tabRenderer": {"selected": True}}]
try:
    renderer = extract_selected_tab_wrapper(tabs)
except ExtractorError as e:
    print(e)

# Stop coverage
cov.stop()
cov.save()

# Write the branch coverage information to a file
with open("branch_coverage_1.json", "w") as f:
    json.dump(branch_coverage_1, f)

# Generate coverage report
cov.report(file='coverage_report_1.txt')

# Print coverage report
cov.report()
