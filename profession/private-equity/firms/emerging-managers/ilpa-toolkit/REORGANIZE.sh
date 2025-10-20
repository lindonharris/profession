#!/bin/bash
# ILPA Toolkit Reorganization Script
# Purpose: Reorganize flat directory into lifecycle-based structure
# Safety: Preserves all files, moves (doesn't copy) to avoid duplication

set -e  # Exit on error

TOOLKIT_DIR="/mnt/c/Users/lindo/Documents/obsidian/profession/private-equity/firms/emerging-managers/ilpa-toolkit"
cd "$TOOLKIT_DIR"

echo "=== ILPA Toolkit Reorganization ==="
echo "Working directory: $TOOLKIT_DIR"
echo ""

# Create directory structure
echo "Creating directory structure..."
mkdir -p 1-foundation
mkdir -p 2-pre-fundraising
mkdir -p 3-fundraising/ddq
mkdir -p 3-fundraising/legal-docs/lpa
mkdir -p 3-fundraising/legal-docs/subscription
mkdir -p 4-operations/reporting
mkdir -p 4-operations/capital-activity
mkdir -p 4-operations/subscription-lines

echo "Directory structure created."
echo ""

# 1. Foundation - Principles
echo "Moving foundation files..."
mv ilpa-principles.md 1-foundation/
mv ILPA-Principles-3.0_2019.pdf 1-foundation/

# 2. Pre-Fundraising - NDA
echo "Moving pre-fundraising files..."
mv model-nda.md 2-pre-fundraising/
mv 2021.1.14-ILPA-Model-NDA.docx 2-pre-fundraising/
mv 2021.1.14-ILPA-Model-NDA.pdf 2-pre-fundraising/

# 3. Fundraising - DDQ
echo "Moving DDQ files..."
mv ddq-diversity-metrics.md 3-fundraising/ddq/
mv ILPA-DDQ-2.0.docx 3-fundraising/ddq/
mv ILPA-DDQ-2.0-User-Guide.pdf 3-fundraising/ddq/

# 3. Fundraising - LPA
echo "Moving LPA files..."
mv model-lpa-overview.md 3-fundraising/legal-docs/lpa/
mv 2020.07.29-ILPA-Model-LPA-Overview-WOF-Version.docx 3-fundraising/legal-docs/lpa/
mv 2020.07.29-ILPA-Model-LPA-Overview-DBD-Version.docx 3-fundraising/legal-docs/lpa/
mv ILPA-Model-Limited-Partnership-Agreement-WOF.docx 3-fundraising/legal-docs/lpa/
mv ILPA-Model-Limited-Partnership-Agreement-WOF.pdf 3-fundraising/legal-docs/lpa/
mv ILPA-Model-Limited-Parnership-Agreement-Deal-By-Deal.docx 3-fundraising/legal-docs/lpa/
mv ILPA-Model-Limited-Parnership-Agreement-Deal-By-Deal.pdf 3-fundraising/legal-docs/lpa/

# 3. Fundraising - Subscription Agreement
echo "Moving Subscription Agreement files..."
mv model-subscription-agreement.md 3-fundraising/legal-docs/subscription/
mv ILPA-Model-Subscription-Agreement-Final.docx 3-fundraising/legal-docs/subscription/
mv ILPA-Model-Subscription-Agreement-Final.pdf 3-fundraising/legal-docs/subscription/

# 4. Operations - Reporting
echo "Moving reporting files..."
mv reporting-template.md 4-operations/reporting/
mv ILPA-Reporting-Template-and-Supplemental-Guidance 4-operations/reporting/

# 4. Operations - Capital Activity
echo "Moving capital activity files..."
mv capital-call-distribution-template.md 4-operations/capital-activity/

# 4. Operations - Subscription Lines
echo "Moving subscription lines files..."
mv subscription-lines-guidance.md 4-operations/subscription-lines/
mv ILPA-Subscription-Lines-of-Credit-and-Alignment-of-Interests-June-2017.pdf 4-operations/subscription-lines/
mv ILPA-Guidance-on-Disclosures-Related-to-Subscription-Lines-of-Credit_2020_FINAL.pdf 4-operations/subscription-lines/

echo ""
echo "=== Reorganization Complete ==="
echo ""
echo "New structure:"
echo "  1-foundation/               (2 files)"
echo "  2-pre-fundraising/          (3 files)"
echo "  3-fundraising/              (13 files in subfolders)"
echo "    ├── ddq/                  (3 files)"
echo "    └── legal-docs/"
echo "        ├── lpa/              (7 files)"
echo "        └── subscription/     (3 files)"
echo "  4-operations/               (13 files in subfolders)"
echo "    ├── reporting/            (2 items: 1 .md + 1 folder)"
echo "    ├── capital-activity/     (1 file)"
echo "    └── subscription-lines/   (3 files)"
echo ""
echo "README files have been created separately."
echo "All wiki-links remain functional (Obsidian resolves by filename)."
echo ""
