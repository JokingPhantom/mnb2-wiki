# Mud and Blood 2 player wiki

Curated project-authored player reference and original instructional diagrams.
Preserve the edition, evidence and source qualifications in every article.
Only the exact admitted diagrams are included; original game media is excluded.

Use Python 3.14 or newer. Install requirements.txt into a local virtual environment.
Build with `python scripts/export-public-wiki.py --output site --base /wiki/`.
The output directory must be new. Serve the resulting directory at /wiki/.

Edit Markdown under research/mnb2/wiki/player/. The source manifest pins each
article's SHA-256; update its hash when approving an edit. Content commits do not
publish the live site. A human requests a release and the publishing agent builds
and deploys that selected committed revision.
