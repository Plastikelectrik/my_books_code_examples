T = $(HOME)/studio/targets/kettle/bin/kettle-stripped
E = $(HOME)/studio/evidence/kettle
C = $(HOME)/studio/captures
S = $(HOME)/studio/scripts

all: overview observations index

overview:
	rea analyze "$(T)" --provider ghidra --json \
	  > "$(E)/overview.json"

observations:
	python3 "$(S)/observe.py" "$(T)" \
	  "$(C)/kettle-observations.csv"

index:
	python3 "$(S)/index_evidence.py" "$(E)" \
	  > "$(E)/INDEX.md"
