---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
NodeJs ^uIcN1gXC

Event
Loop ^WKrgFgeU

Timers ^Pmcqk03k

It looks for timers like:
setTimeout(), setInterval() ^JeiIGBwb

nextTick() queue ^ZdQhfeyu

Micro Task queue ^q5HmOtIm

Macro Task queue ^TBGzW68F

v8 is a JavaScript engine and
it manages a CALL STACK ^eW9Wb8TJ

Pending callbacks ^OHjWkVh7

Idle, prepare ^rPilRBfr

Pool ^VA3WqCym

Check ^24wz5XTR

Close callbacks ^qnJRpU0m

setImmediate() ^HuKxGzc4

Javascript ^C7KScaGX

Can't run things in parallel
It only can do one thing at a time ^Yl7Qf89O

Every time we call a function
we added it to the callstack ^roSobXTO

if the function take some time to finish 
the function will be dump it off to the LIBUV ^nq48JZsW

After the function is finished, LIBUV will
send it to the EVENT QUEUE ^zTG9Q8l8

Event loop is watching the EVENT QUEUE
for finished functions to be pick up ^HbFIB9zL

This happens because javascript has a only
single callstack ^VLdOKy9S

WebApis are similar to the LIBUV, but
they run on the browser ecosystem ^Yvhfqlf0

Written in C++ ^WJ4u67o5

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.28",
	"elements": [
		{
			"type": "text",
			"version": 18,
			"versionNonce": 1345308927,
			"isDeleted": false,
			"id": "uIcN1gXC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -82.76458740234375,
			"y": -62.902503967285156,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 69.81993103027344,
			"height": 25,
			"seed": 1535468369,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "oLGGf2W1Ye6-xpjK12oDY",
					"type": "arrow"
				},
				{
					"id": "rIDCPRxwofeRdMemtjHVZ",
					"type": "arrow"
				},
				{
					"id": "kyoWxfd128SQEggsm0wbP",
					"type": "arrow"
				}
			],
			"updated": 1728093999294,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "NodeJs",
			"rawText": "NodeJs",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "NodeJs",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "ellipse",
			"version": 123,
			"versionNonce": 1104395729,
			"isDeleted": false,
			"id": "J_E3AbCx7lukPjcTKWByb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 95.99804056870312,
			"y": -319.26675644715476,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 215.4375,
			"height": 215.4375,
			"seed": 1175440383,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"id": "1IuEErTAu7n-C4kqJiXI-",
					"type": "arrow"
				},
				{
					"id": "B5TJIcYi4OXnqN1lve9DW",
					"type": "arrow"
				},
				{
					"type": "text",
					"id": "WKrgFgeU"
				},
				{
					"id": "oLGGf2W1Ye6-xpjK12oDY",
					"type": "arrow"
				},
				{
					"id": "T1VEa6FxJBHfByrppwUvJ",
					"type": "arrow"
				},
				{
					"id": "rMFVVE3vxyaeSHTNwBWfv",
					"type": "arrow"
				},
				{
					"id": "zBxsOB3WACBvI-N47HlZY",
					"type": "arrow"
				}
			],
			"updated": 1728094371890,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 79,
			"versionNonce": 2031460849,
			"isDeleted": false,
			"id": "WKrgFgeU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 175.7881527347178,
			"y": -236.7166650330932,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 55.51995849609375,
			"height": 50,
			"seed": 1107639761,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093701646,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Event\nLoop",
			"rawText": "Event\nLoop",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "J_E3AbCx7lukPjcTKWByb",
			"originalText": "Event\nLoop",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 184,
			"versionNonce": 492050849,
			"isDeleted": false,
			"id": "1IuEErTAu7n-C4kqJiXI-",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 109.33932225902745,
			"y": -262.7682812920037,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 8.876636683462834,
			"height": 13.302995126671647,
			"seed": 547983793,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 1,
				"focus": 0.9898665912124618
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					8.876636683462834,
					-13.302995126671647
				],
				[
					1.4363495778527806,
					-5.186418467555939
				]
			]
		},
		{
			"type": "arrow",
			"version": 398,
			"versionNonce": 1170357633,
			"isDeleted": false,
			"id": "B5TJIcYi4OXnqN1lve9DW",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 306.8123951100709,
			"y": -181.1392483120618,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 11.321939352890752,
			"height": 26.382374926845202,
			"seed": 830174015,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 1,
				"focus": 0.9917519147388086
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-11.321939352890752,
					26.382374926845202
				],
				[
					-8.211074023172785,
					22.663762719905264
				]
			]
		},
		{
			"type": "rectangle",
			"version": 99,
			"versionNonce": 555804095,
			"isDeleted": false,
			"id": "8z-THKv8zVBNlOIL3AeTl",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 362.92124180260396,
			"y": -410.78070228599177,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.8032476204802,
			"height": 419.32266608077595,
			"seed": 983250417,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"id": "T1VEa6FxJBHfByrppwUvJ",
					"type": "arrow"
				}
			],
			"updated": 1728093701646,
			"link": null,
			"locked": false
		},
		{
			"type": "rectangle",
			"version": 124,
			"versionNonce": 1159499359,
			"isDeleted": false,
			"id": "Z3VRcS3-_vnncDNrTWSL3",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 374.45884257324894,
			"y": -387.5880144893174,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 217688209,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "Pmcqk03k"
				}
			],
			"updated": 1728093716867,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 49,
			"versionNonce": 1482254975,
			"isDeleted": false,
			"id": "Pmcqk03k",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 450.06290162358624,
			"y": -374.769339386492,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 63.519927978515625,
			"height": 25,
			"seed": 1977826353,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093716867,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Timers",
			"rawText": "Timers",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Z3VRcS3-_vnncDNrTWSL3",
			"originalText": "Timers",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 59,
			"versionNonce": 819958081,
			"isDeleted": false,
			"id": "oLGGf2W1Ye6-xpjK12oDY",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -6.591276381715382,
			"y": -71.00886581026539,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 106.0428968771707,
			"height": 75.2904408300672,
			"seed": 576438431,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uIcN1gXC",
				"gap": 10.299443656390793,
				"focus": 0.23307919544400402
			},
			"endBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 15.27969924585058,
				"focus": 0.06645732966460288
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					106.0428968771707,
					-75.2904408300672
				]
			]
		},
		{
			"type": "arrow",
			"version": 124,
			"versionNonce": 806024449,
			"isDeleted": false,
			"id": "T1VEa6FxJBHfByrppwUvJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 318.1873118182868,
			"y": -238.47884821579288,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 33.50177076505696,
			"height": 3.62308243048642,
			"seed": 1457659249,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 9.877042754327789,
				"focus": -0.1376914935017092
			},
			"endBinding": {
				"elementId": "8z-THKv8zVBNlOIL3AeTl",
				"gap": 11.232159219260211,
				"focus": 0.24742042266323025
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					33.50177076505696,
					-3.62308243048642
				]
			]
		},
		{
			"type": "text",
			"version": 88,
			"versionNonce": 1695588721,
			"isDeleted": false,
			"id": "JeiIGBwb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 690.4078835415064,
			"y": -372.79823076526276,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 269.39971923828125,
			"height": 50,
			"seed": 1005773585,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "R6qQg2UB0YrDF4EI0O6NB",
					"type": "arrow"
				}
			],
			"updated": 1728093701646,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "It looks for timers like:\nsetTimeout(), setInterval()",
			"rawText": "It looks for timers like:\nsetTimeout(), setInterval()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "It looks for timers like:\nsetTimeout(), setInterval()",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 51,
			"versionNonce": 718875167,
			"isDeleted": false,
			"id": "R6qQg2UB0YrDF4EI0O6NB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 588.9981310447015,
			"y": -316.1735126407373,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 93.68816873629191,
			"height": 29.341901269138816,
			"seed": 1529597311,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728093701646,
			"link": null,
			"locked": false,
			"startBinding": null,
			"endBinding": {
				"elementId": "JeiIGBwb",
				"focus": 0.6299164123984495,
				"gap": 7.721583760512999
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					93.68816873629191,
					-29.341901269138816
				]
			]
		},
		{
			"type": "ellipse",
			"version": 93,
			"versionNonce": 1782480479,
			"isDeleted": false,
			"id": "2SZ8M77xsrZ181751BDCg",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 365.1244147039424,
			"y": 37.21998461655778,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.44705493163764,
			"height": 97.26742065841609,
			"seed": 664477631,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "ZdQhfeyu"
				}
			],
			"updated": 1728094711779,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 48,
			"versionNonce": 1264036001,
			"isDeleted": false,
			"id": "ZdQhfeyu",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 429.8377790300668,
			"y": 60.964468577720574,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 108.11990356445312,
			"height": 50,
			"seed": 822399,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728237654800,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "nextTick() \nqueue",
			"rawText": "nextTick() queue",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "2SZ8M77xsrZ181751BDCg",
			"originalText": "nextTick() queue",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "ellipse",
			"version": 116,
			"versionNonce": 1565242015,
			"isDeleted": false,
			"id": "tpqS3059OkxJi4XDHevOr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 370.8628850635515,
			"y": 155.92516111099894,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.44705493163764,
			"height": 97.26742065841609,
			"seed": 2081330239,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "q5HmOtIm"
				}
			],
			"updated": 1728094711779,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 88,
			"versionNonce": 530187967,
			"isDeleted": false,
			"id": "q5HmOtIm",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 429.91624572756655,
			"y": 179.66964507216173,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 119.43991088867188,
			"height": 50,
			"seed": 1389343839,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728094711779,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Micro Task \nqueue",
			"rawText": "Micro Task queue",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "tpqS3059OkxJi4XDHevOr",
			"originalText": "Micro Task queue",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "ellipse",
			"version": 179,
			"versionNonce": 1423280049,
			"isDeleted": false,
			"id": "-5DtugPBLSqb3Kt09Hp-s",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 373.82580855166884,
			"y": 275.4441757551606,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 237.44705493163764,
			"height": 97.26742065841609,
			"seed": 1071696273,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [
				{
					"type": "text",
					"id": "TBGzW68F"
				}
			],
			"updated": 1728094715423,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 154,
			"versionNonce": 1426811281,
			"isDeleted": false,
			"id": "TBGzW68F",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 428.3991658587503,
			"y": 299.1886597163234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 128.39991760253906,
			"height": 50,
			"seed": 622030705,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728094715423,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Macro Task \nqueue",
			"rawText": "Macro Task queue",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "-5DtugPBLSqb3Kt09Hp-s",
			"originalText": "Macro Task queue",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "text",
			"version": 118,
			"versionNonce": 858474767,
			"isDeleted": false,
			"id": "eW9Wb8TJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -200.34671701508069,
			"y": 100.01905607990568,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 299.519775390625,
			"height": 50,
			"seed": 986667185,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "rIDCPRxwofeRdMemtjHVZ",
					"type": "arrow"
				}
			],
			"updated": 1728246549176,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "v8 is a JavaScript engine and\nit manages a CALL STACK",
			"rawText": "v8 is a JavaScript engine and\nit manages a CALL STACK",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "v8 is a JavaScript engine and\nit manages a CALL STACK",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 266,
			"versionNonce": 1142771503,
			"isDeleted": false,
			"id": "rIDCPRxwofeRdMemtjHVZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -162.07196433499524,
			"y": -169.18796492383728,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 141.87164060981252,
			"height": 258.68593861425813,
			"seed": 1484169055,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728246549177,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "C7KScaGX",
				"focus": 0.1525727535753254,
				"gap": 9.032100144188178
			},
			"endBinding": {
				"elementId": "eW9Wb8TJ",
				"focus": 0.41202363447123047,
				"gap": 10.521082389484832
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					26.557382058356495,
					165.82329458010042
				],
				[
					141.87164060981252,
					258.68593861425813
				]
			]
		},
		{
			"type": "rectangle",
			"version": 153,
			"versionNonce": 65389215,
			"isDeleted": false,
			"id": "RvFckFDwM7uYuznvUkpOa",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 374.5183581540239,
			"y": -325.415368593347,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 1879121087,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "OHjWkVh7"
				}
			],
			"updated": 1728093716867,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 97,
			"versionNonce": 141694655,
			"isDeleted": false,
			"id": "OHjWkVh7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 398.5524480271151,
			"y": -312.5966934905216,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 166.6598663330078,
			"height": 25,
			"seed": 677194975,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093716867,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Pending callbacks",
			"rawText": "Pending callbacks",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "RvFckFDwM7uYuznvUkpOa",
			"originalText": "Pending callbacks",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "rectangle",
			"version": 181,
			"versionNonce": 1329763121,
			"isDeleted": false,
			"id": "6O95pK-PtDNbYMvV8dIuT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 375.8692196647721,
			"y": -257.0464829189234,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 1557579697,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "rPilRBfr"
				}
			],
			"updated": 1728093720284,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 141,
			"versionNonce": 617284881,
			"isDeleted": false,
			"id": "rPilRBfr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 420.353298856711,
			"y": -244.227807816098,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 125.7598876953125,
			"height": 25,
			"seed": 1256499601,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093720284,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Idle, prepare",
			"rawText": "Idle, prepare",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "6O95pK-PtDNbYMvV8dIuT",
			"originalText": "Idle, prepare",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "rectangle",
			"version": 237,
			"versionNonce": 1847173777,
			"isDeleted": false,
			"id": "b8rgeFnzRsEft6DFHzfFn",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 376.95178101765293,
			"y": -193.22320003239912,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 864860881,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "VA3WqCym"
				}
			],
			"updated": 1728093733320,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 206,
			"versionNonce": 1643536305,
			"isDeleted": false,
			"id": "VA3WqCym",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 463.9958272506074,
			"y": -180.4045249295737,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 40.63995361328125,
			"height": 25,
			"seed": 951007409,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093734891,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Pool",
			"rawText": "Pool",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "b8rgeFnzRsEft6DFHzfFn",
			"originalText": "Pool",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "rectangle",
			"version": 268,
			"versionNonce": 856149503,
			"isDeleted": false,
			"id": "EScH78ni-59UnPXud-l30",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 377.545396636532,
			"y": -127.37067686034709,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 1406445855,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "24wz5XTR"
				},
				{
					"id": "GLZtNcA2MtvEVdPU56ONZ",
					"type": "arrow"
				}
			],
			"updated": 1728093796356,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 239,
			"versionNonce": 506028753,
			"isDeleted": false,
			"id": "24wz5XTR",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 458.1694447005412,
			"y": -114.55200175752168,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 53.479949951171875,
			"height": 25,
			"seed": 1992305983,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093733308,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Check",
			"rawText": "Check",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "EScH78ni-59UnPXud-l30",
			"originalText": "Check",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "rectangle",
			"version": 271,
			"versionNonce": 483679729,
			"isDeleted": false,
			"id": "Hl_SdHL1WZtZJAhTQDK4z",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 374.0491064053298,
			"y": -63.4605641651429,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 214.72804607919022,
			"height": 50.63735020565082,
			"seed": 2104021329,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 3
			},
			"boundElements": [
				{
					"type": "text",
					"id": "qnJRpU0m"
				}
			],
			"updated": 1728093738267,
			"link": null,
			"locked": false
		},
		{
			"type": "text",
			"version": 253,
			"versionNonce": 1827658609,
			"isDeleted": false,
			"id": "qnJRpU0m",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 406.88319170078427,
			"y": -50.64188906231749,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 149.05987548828125,
			"height": 25,
			"seed": 1271168817,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728093764647,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Close callbacks",
			"rawText": "Close callbacks",
			"textAlign": "center",
			"verticalAlign": "middle",
			"containerId": "Hl_SdHL1WZtZJAhTQDK4z",
			"originalText": "Close callbacks",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "text",
			"version": 16,
			"versionNonce": 377330239,
			"isDeleted": false,
			"id": "HuKxGzc4",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 704.922113789066,
			"y": -97.762967833772,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 146.65985107421875,
			"height": 25,
			"seed": 1840854079,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "GLZtNcA2MtvEVdPU56ONZ",
					"type": "arrow"
				}
			],
			"updated": 1728093796356,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "setImmediate()",
			"rawText": "setImmediate()",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "setImmediate()",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "arrow",
			"version": 33,
			"versionNonce": 1210889313,
			"isDeleted": false,
			"id": "GLZtNcA2MtvEVdPU56ONZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 593.2734427157222,
			"y": -99.55551827908191,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 103.46667115259186,
			"height": 15.429237241198152,
			"seed": 1684894001,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654804,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "EScH78ni-59UnPXud-l30",
				"gap": 1,
				"focus": -0.33059180341954875
			},
			"endBinding": {
				"elementId": "HuKxGzc4",
				"gap": 8.181999920751878,
				"focus": -0.567180690673971
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					103.46667115259186,
					15.429237241198152
				]
			]
		},
		{
			"type": "text",
			"version": 16,
			"versionNonce": 1629526255,
			"isDeleted": false,
			"id": "C7KScaGX",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -209.64556306978307,
			"y": -203.22006506802546,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 104.85990905761719,
			"height": 25,
			"seed": 1011654417,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "kyoWxfd128SQEggsm0wbP",
					"type": "arrow"
				},
				{
					"id": "06saTRKgx2wLmeff2kYMb",
					"type": "arrow"
				},
				{
					"id": "rMFVVE3vxyaeSHTNwBWfv",
					"type": "arrow"
				},
				{
					"id": "jzDuuIByXRNhbRcfGejn4",
					"type": "arrow"
				},
				{
					"id": "rIDCPRxwofeRdMemtjHVZ",
					"type": "arrow"
				}
			],
			"updated": 1728246513313,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Javascript",
			"rawText": "Javascript",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Javascript",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "text",
			"version": 135,
			"versionNonce": 1212462305,
			"isDeleted": false,
			"id": "Yl7Qf89O",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -292.4350981998551,
			"y": -336.8221024125603,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 345.979736328125,
			"height": 50,
			"seed": 1445752831,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "06saTRKgx2wLmeff2kYMb",
					"type": "arrow"
				},
				{
					"id": "tRTekV4ZCCOY7jdegPteo",
					"type": "arrow"
				}
			],
			"updated": 1728246075053,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Can't run things in parallel\nIt only can do one thing at a time",
			"rawText": "Can't run things in parallel\nIt only can do one thing at a time",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Can't run things in parallel\nIt only can do one thing at a time",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 27,
			"versionNonce": 510415135,
			"isDeleted": false,
			"id": "kyoWxfd128SQEggsm0wbP",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -55.09631435125493,
			"y": -75.03513624598969,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.63818163848282,
			"height": 89.09306700079719,
			"seed": 1207453105,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728093999294,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "uIcN1gXC",
				"focus": 0.2899530702430641,
				"gap": 12.132632278704534
			},
			"endBinding": {
				"elementId": "C7KScaGX",
				"focus": -0.10360021529894786,
				"gap": 14.09186182123858
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-73.63818163848282,
					-89.09306700079719
				]
			]
		},
		{
			"type": "arrow",
			"version": 191,
			"versionNonce": 972271777,
			"isDeleted": false,
			"id": "06saTRKgx2wLmeff2kYMb",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -157.4947898233602,
			"y": -215.03855329748757,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 12.56635343324453,
			"height": 59.50991625221292,
			"seed": 213112159,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728246075054,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "C7KScaGX",
				"focus": -0.09160163277078641,
				"gap": 11.818488229462105
			},
			"endBinding": {
				"elementId": "Yl7Qf89O",
				"focus": 0.0987965327837743,
				"gap": 12.273632862859813
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					12.56635343324453,
					-59.50991625221292
				]
			]
		},
		{
			"type": "text",
			"version": 185,
			"versionNonce": 355482225,
			"isDeleted": false,
			"id": "roSobXTO",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 293.09395373118207,
			"y": -553.2285925007935,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 290.8997802734375,
			"height": 50,
			"seed": 1818063743,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "rMFVVE3vxyaeSHTNwBWfv",
					"type": "arrow"
				},
				{
					"id": "ZZK8xbXRjNvChprV0nXHD",
					"type": "arrow"
				}
			],
			"updated": 1728094259282,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Every time we call a function\nwe added it to the callstack",
			"rawText": "Every time we call a function\nwe added it to the callstack",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Every time we call a function\nwe added it to the callstack",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 291,
			"versionNonce": 1204202721,
			"isDeleted": false,
			"id": "rMFVVE3vxyaeSHTNwBWfv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 263.82139872739356,
			"y": -327.7684751893985,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 105.44454404000624,
			"height": 165.44346085243342,
			"seed": 221061649,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 23.12375561868862,
				"focus": 0.08873046588046822
			},
			"endBinding": {
				"elementId": "roSobXTO",
				"focus": 0.22513892840695715,
				"gap": 10.01665645896162
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					39.272905450729695,
					-91.82050161422285
				],
				[
					105.44454404000624,
					-165.44346085243342
				]
			]
		},
		{
			"type": "text",
			"version": 101,
			"versionNonce": 1898842785,
			"isDeleted": false,
			"id": "nq48JZsW",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 464.91637755430816,
			"y": -670.8009226735132,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 454.859619140625,
			"height": 50,
			"seed": 334182399,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ZZK8xbXRjNvChprV0nXHD",
					"type": "arrow"
				},
				{
					"id": "p-YwPpecgo2Zg7GR9Ojt-",
					"type": "arrow"
				},
				{
					"id": "Q0jp3wlDcPI2AVqKHnS51",
					"type": "arrow"
				}
			],
			"updated": 1728246133830,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "if the function take some time to finish \nthe function will be dump it off to the LIBUV",
			"rawText": "if the function take some time to finish \nthe function will be dump it off to the LIBUV",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "if the function take some time to finish \nthe function will be dump it off to the LIBUV",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 37,
			"versionNonce": 140666543,
			"isDeleted": false,
			"id": "ZZK8xbXRjNvChprV0nXHD",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 474.0075831301074,
			"y": -564.137920663137,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 55.473909841776845,
			"height": 46.66152236375797,
			"seed": 188631263,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728246124113,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "roSobXTO",
				"focus": -0.03745628755537341,
				"gap": 10.909328162343513
			},
			"endBinding": {
				"elementId": "nq48JZsW",
				"focus": 0.47152372349821586,
				"gap": 10.001479646618236
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					55.473909841776845,
					-46.66152236375797
				]
			]
		},
		{
			"type": "text",
			"version": 76,
			"versionNonce": 771051025,
			"isDeleted": false,
			"id": "zTG9Q8l8",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 569.4644514852304,
			"y": -824.5583265786267,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 402.73968505859375,
			"height": 50,
			"seed": 778117503,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "p-YwPpecgo2Zg7GR9Ojt-",
					"type": "arrow"
				},
				{
					"id": "zBxsOB3WACBvI-N47HlZY",
					"type": "arrow"
				}
			],
			"updated": 1728094371890,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "After the function is finished, LIBUV will\nsend it to the EVENT QUEUE",
			"rawText": "After the function is finished, LIBUV will\nsend it to the EVENT QUEUE",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "After the function is finished, LIBUV will\nsend it to the EVENT QUEUE",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 24,
			"versionNonce": 1949157103,
			"isDeleted": false,
			"id": "p-YwPpecgo2Zg7GR9Ojt-",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 600.9656452784864,
			"y": -678.4878832737601,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 91.65783559876195,
			"height": 85.15986437503545,
			"seed": 1120938641,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728246124113,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "nq48JZsW",
				"focus": -0.49721215982479017,
				"gap": 7.6869606002468345
			},
			"endBinding": {
				"elementId": "zTG9Q8l8",
				"focus": 0.17329852940273313,
				"gap": 10.910578929831217
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					91.65783559876195,
					-85.15986437503545
				]
			]
		},
		{
			"type": "arrow",
			"version": 159,
			"versionNonce": 50358465,
			"isDeleted": false,
			"id": "zBxsOB3WACBvI-N47HlZY",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 557.6459328638157,
			"y": -800.9213805116556,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 370.008954799077,
			"height": 474.5570287299993,
			"seed": 1164397023,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728237654797,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "zTG9Q8l8",
				"focus": 0.9098423431000406,
				"gap": 11.818518621414682
			},
			"endBinding": {
				"elementId": "J_E3AbCx7lukPjcTKWByb",
				"gap": 8.218101458602945,
				"focus": -0.44342474381067404
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-291.82523115659984,
					208.1868814228917
				],
				[
					-370.008954799077,
					474.5570287299993
				]
			]
		},
		{
			"type": "text",
			"version": 155,
			"versionNonce": 78833279,
			"isDeleted": false,
			"id": "HbFIB9zL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -89.64248220873617,
			"y": -686.3731080935553,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 416.51971435546875,
			"height": 50,
			"seed": 1698438623,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [],
			"updated": 1728094405482,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "Event loop is watching the EVENT QUEUE\nfor finished functions to be pick up",
			"rawText": "Event loop is watching the EVENT QUEUE\nfor finished functions to be pick up",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Event loop is watching the EVENT QUEUE\nfor finished functions to be pick up",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "text",
			"version": 99,
			"versionNonce": 1577851743,
			"isDeleted": false,
			"id": "VLdOKy9S",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -471.4700164131332,
			"y": -486.3682569833683,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 434.1396484375,
			"height": 50,
			"seed": 1369215679,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "tRTekV4ZCCOY7jdegPteo",
					"type": "arrow"
				}
			],
			"updated": 1728094700611,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "This happens because javascript has a only\nsingle callstack",
			"rawText": "This happens because javascript has a only\nsingle callstack",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "This happens because javascript has a only\nsingle callstack",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 362,
			"versionNonce": 895925345,
			"isDeleted": false,
			"id": "tRTekV4ZCCOY7jdegPteo",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -170.6710024159855,
			"y": -350.8728339751801,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 163.2582860951383,
			"height": 84.49542300818825,
			"seed": 426644881,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728246075054,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Yl7Qf89O",
				"focus": 0.1097390186348189,
				"gap": 14.050731562619774
			},
			"endBinding": {
				"elementId": "VLdOKy9S",
				"focus": 0.4889901747019696,
				"gap": 1
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-163.2582860951383,
					-84.49542300818825
				]
			]
		},
		{
			"type": "text",
			"version": 177,
			"versionNonce": 2097583647,
			"isDeleted": false,
			"id": "Yvhfqlf0",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -664.0888626426329,
			"y": -115.31987988277717,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 381.0997314453125,
			"height": 50,
			"seed": 566648927,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "jzDuuIByXRNhbRcfGejn4",
					"type": "arrow"
				}
			],
			"updated": 1728095043377,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "WebApis are similar to the LIBUV, but\nthey run on the browser ecosystem",
			"rawText": "WebApis are similar to the LIBUV, but\nthey run on the browser ecosystem",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "WebApis are similar to the LIBUV, but\nthey run on the browser ecosystem",
			"lineHeight": 1.25,
			"baseline": 42
		},
		{
			"type": "arrow",
			"version": 26,
			"versionNonce": 1665194591,
			"isDeleted": false,
			"id": "jzDuuIByXRNhbRcfGejn4",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -216.89330897192127,
			"y": -170.15720688558514,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 71.33818734329037,
			"height": 43.21588971612414,
			"seed": 917848849,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1728095043378,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "C7KScaGX",
				"focus": 0.37689964679897436,
				"gap": 10.841563666376999
			},
			"endBinding": {
				"elementId": "Yvhfqlf0",
				"focus": 0.5385899470752045,
				"gap": 11.621437286683829
			},
			"lastCommittedPoint": null,
			"startArrowhead": null,
			"endArrowhead": "arrow",
			"points": [
				[
					0,
					0
				],
				[
					-71.33818734329037,
					43.21588971612414
				]
			]
		},
		{
			"id": "WJ4u67o5",
			"type": "text",
			"x": 1054.34445523485,
			"y": -643.3497903316736,
			"width": 142.37991333007812,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1082887009,
			"version": 16,
			"versionNonce": 1364366945,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Q0jp3wlDcPI2AVqKHnS51",
					"type": "arrow"
				}
			],
			"updated": 1728246133830,
			"link": null,
			"locked": false,
			"text": "Written in C++",
			"rawText": "Written in C++",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Written in C++",
			"lineHeight": 1.25
		},
		{
			"id": "Q0jp3wlDcPI2AVqKHnS51",
			"type": "arrow",
			"x": 931.1069470968295,
			"y": -643.3497903316736,
			"width": 114.10888671875011,
			"height": 10.650177001953125,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 153245999,
			"version": 23,
			"versionNonce": 1261833857,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1728246133830,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					114.10888671875011,
					10.650177001953125
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "nq48JZsW",
				"focus": -0.42904182209854425,
				"gap": 11.330950401896303
			},
			"endBinding": {
				"elementId": "WJ4u67o5",
				"focus": -0.29494715006919553,
				"gap": 9.12862141927053
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "Oau0ZJAs",
			"type": "text",
			"x": 28.500745924954344,
			"y": -349.9997231930017,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2089435201,
			"version": 2,
			"versionNonce": 1980677743,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1728246052562,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		}
	],
	"appState": {
		"theme": "light",
		"viewBackgroundColor": "#ffffff",
		"currentItemStrokeColor": "#1e1e1e",
		"currentItemBackgroundColor": "transparent",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 2,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 585.0531564953886,
		"scrollY": 560.3694508325924,
		"zoom": {
			"value": 0.8500000000000002
		},
		"currentItemRoundness": "round",
		"gridSize": null,
		"gridColor": {
			"Bold": "#C9C9C9FF",
			"Regular": "#EDEDEDFF"
		},
		"currentStrokeOptions": null,
		"previousGridSize": null,
		"frameRendering": {
			"enabled": true,
			"clip": true,
			"name": true,
			"outline": true
		}
	},
	"files": {}
}
```
%%