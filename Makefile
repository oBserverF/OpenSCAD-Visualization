TARGETS := Ui_KinematicScheme.py
TARGETS += joint0.wrl joint1.wrl joint2.wrl joint3.wrl joint4.wrl joint5.wrl

.PHONY: all
all: ${TARGETS}

Ui_KinematicScheme.py: KinematicScheme.ui
	uic -g python -o Ui_KinematicScheme.py KinematicScheme.ui

joint0.wrl: joint.scad joint.json
	openscad -o joint0.wrl -p joint.json -P joint0 -D debug=false joint.scad

joint1.wrl: joint.scad joint.json
	openscad -o joint1.wrl -p joint.json -P joint1 -D debug=false joint.scad

joint2.wrl: joint.scad joint.json
	openscad -o joint2.wrl -p joint.json -P joint2 -D debug=false joint.scad

joint3.wrl: joint.scad joint.json
	openscad -o joint3.wrl -p joint.json -P joint3 -D debug=false joint.scad

joint4.wrl: joint.scad joint.json
	openscad -o joint4.wrl -p joint.json -P joint4 -D debug=false joint.scad

joint5.wrl: joint.scad joint.json
	openscad -o joint5.wrl -p joint.json -P joint5 -D debug=false joint.scad

.PHONY: distclean
distclean:
	${RM} ${TARGETS}
