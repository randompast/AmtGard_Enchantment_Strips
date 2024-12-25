rm spells.json
wget https://raw.githubusercontent.com/kenwalker/easygard.ca/refs/heads/master/spells.json

sed -i 's/\\“/\\"/g' spells.json
sed -i 's/\\”/\\"/g' spells.json
sed -i 's/“/\\"/g' spells.json
sed -i 's/”/\\"/g' spells.json
sed -i 's/<br>/ /g' spells.json
python3 strips.py