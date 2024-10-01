---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
SSH ^mtcNJo8a

ssh-keygen

* ssh-keygen [-t dsa | ed25519 | rsa] ^NUKmDh4u

~/.ssh ^WIFakPxQ

It is a folder that store
public and private keys and
also a folder called "authorized_keys" ^Jx8tV9SG

Access remote machine ^jYo7Rnys

ssh -l user <remote-server-ip>
                ||
ssh user@<remote-server-ip> ^BRJFI3LA

ssh-copy-id -i public/key/path user@<remote-server-ip>

                        ||
cat ~/.ssh/id_rsa.pub | ssh kakaroto@192.168.1.3 'cat >> ~/.ssh/authorized_keys'

                        ||

scp /file/path user@server:/path/directory ^85eOM8Pg

Create Alias ^kXu8CRVt

vim ~/.ssh/config

file content:

Host snakecave
    HostName 192.168.1.3
    User kakaroto ^Pgez5puV

Additional info ^uzPS1M4g

Check content inside remote server 
(from host machine) ^JSUMzHeT

Generate new Key ^BhfgxNul

Send key to remote machine: ^Ey27FIiy

SSH Agent ^5oH11oaJ

sudo systemctl restart ssh ^POiyW7CU

Restart SSH service ^v9HcsL9e

Check if daemon allows public key auth ^nRBdutVv

/etc/ssh/sshd_config

content:
 
PublicAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys ^IsiPoUIB

SSH Agent not running

$ eval "$(ssh-agent -s)"
$ ssh-add private/key/path
$ssh-add -l ^vKVfcAOp

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
			"version": 24,
			"versionNonce": 1327010135,
			"isDeleted": false,
			"id": "mtcNJo8a",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -118.36651611328125,
			"y": -85.68268585205078,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 63.61199951171875,
			"height": 45,
			"seed": 1724743991,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "kyD34Xn-CzZlquXjI5wNf",
					"type": "arrow"
				},
				{
					"id": "MJnJYcexv_TKGRHMEkjOF",
					"type": "arrow"
				},
				{
					"id": "qozVLxor0_3S0FSnbeiI7",
					"type": "arrow"
				},
				{
					"id": "mztYY1Dx3tx7kDpQySWR5",
					"type": "arrow"
				},
				{
					"id": "GckQlyVSXVhulanMopHrx",
					"type": "arrow"
				},
				{
					"id": "Oo9U_j-DKabqZucK3GdzZ",
					"type": "arrow"
				},
				{
					"id": "jgj7SqJfn1O1EpJtndtMC",
					"type": "arrow"
				},
				{
					"id": "RE0TKQq9_ewvWMwjgolW7",
					"type": "arrow"
				},
				{
					"id": "KYsAFD1QfiJ7uQzco7MN_",
					"type": "arrow"
				},
				{
					"id": "ayecR-x0MpEBLp8QGzMWK",
					"type": "arrow"
				}
			],
			"updated": 1727486565749,
			"link": null,
			"locked": false,
			"fontSize": 36,
			"fontFamily": 1,
			"text": "SSH",
			"rawText": "SSH",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "SSH",
			"lineHeight": 1.25,
			"baseline": 31
		},
		{
			"type": "text",
			"version": 400,
			"versionNonce": 1885617175,
			"isDeleted": false,
			"id": "NUKmDh4u",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 684.0584436974594,
			"y": 238.2873326527632,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 373.8197021484375,
			"height": 75,
			"seed": 2113006073,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "kyD34Xn-CzZlquXjI5wNf",
					"type": "arrow"
				},
				{
					"id": "dd6aj8-mbvRijCA_AQZP_",
					"type": "arrow"
				}
			],
			"updated": 1727485874838,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "ssh-keygen\n\n* ssh-keygen [-t dsa | ed25519 | rsa]",
			"rawText": "ssh-keygen\n\n* ssh-keygen [-t dsa | ed25519 | rsa]",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ssh-keygen\n\n* ssh-keygen [-t dsa | ed25519 | rsa]",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "arrow",
			"version": 756,
			"versionNonce": 799697337,
			"isDeleted": false,
			"id": "kyD34Xn-CzZlquXjI5wNf",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -48.004214556531934,
			"y": -38.26701649806073,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 445.473500775935,
			"height": 182.44867962728375,
			"seed": 732431255,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485868457,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": 0.25817030547477166,
				"gap": 7.169521331787124
			},
			"endBinding": {
				"elementId": "BhfgxNul",
				"focus": 0.12216978471271124,
				"gap": 8.758588555202266
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
					445.473500775935,
					182.44867962728375
				]
			]
		},
		{
			"type": "text",
			"version": 76,
			"versionNonce": 1753047033,
			"isDeleted": false,
			"id": "WIFakPxQ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 17.74725663678055,
			"y": -181.5037018719343,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 89.4599609375,
			"height": 35,
			"seed": 1407338807,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "MJnJYcexv_TKGRHMEkjOF",
					"type": "arrow"
				},
				{
					"id": "ub9JEK6L_DYvyk0axbD96",
					"type": "arrow"
				}
			],
			"updated": 1727485649181,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "~/.ssh",
			"rawText": "~/.ssh",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "~/.ssh",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 136,
			"versionNonce": 1887664151,
			"isDeleted": false,
			"id": "MJnJYcexv_TKGRHMEkjOF",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -57.89766526245119,
			"y": -94.18289947509766,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 73.47747201229606,
			"height": 49.38217435172061,
			"seed": 1175167481,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485649181,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.27326714981121886,
				"gap": 8.500213623046875
			},
			"endBinding": {
				"elementId": "WIFakPxQ",
				"focus": 0.23295671452986172,
				"gap": 3.6514892578125
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
					73.47747201229606,
					-49.38217435172061
				]
			]
		},
		{
			"type": "text",
			"version": 164,
			"versionNonce": 1705048281,
			"isDeleted": false,
			"id": "Jx8tV9SG",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 198.65115143028163,
			"y": -343.2793475614463,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 381.33966064453125,
			"height": 75,
			"seed": 686681241,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ub9JEK6L_DYvyk0axbD96",
					"type": "arrow"
				}
			],
			"updated": 1727485649181,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "It is a folder that store\npublic and private keys and\nalso a folder called \"authorized_keys\"",
			"rawText": "It is a folder that store\npublic and private keys and\nalso a folder called \"authorized_keys\"",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "It is a folder that store\npublic and private keys and\nalso a folder called \"authorized_keys\"",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "arrow",
			"version": 84,
			"versionNonce": 2074762551,
			"isDeleted": false,
			"id": "ub9JEK6L_DYvyk0axbD96",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 116.70991967622433,
			"y": -180.12003107760054,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 79.24854640513075,
			"height": 75.57115769478915,
			"seed": 1071333655,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485649181,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "WIFakPxQ",
				"focus": 0.5885601352715152,
				"gap": 9.502702101943783
			},
			"endBinding": {
				"elementId": "Jx8tV9SG",
				"focus": 0.6123490993057792,
				"gap": 12.872928807650055
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
					79.24854640513075,
					-75.57115769478915
				]
			]
		},
		{
			"type": "text",
			"version": 117,
			"versionNonce": 117188567,
			"isDeleted": false,
			"id": "jYo7Rnys",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -476.4079603890494,
			"y": -188.1480276036733,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 310.743896484375,
			"height": 35,
			"seed": 812437561,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "qozVLxor0_3S0FSnbeiI7",
					"type": "arrow"
				},
				{
					"id": "83U6Q1SpjVBLa1ptikmtL",
					"type": "arrow"
				}
			],
			"updated": 1727485806185,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Access remote machine",
			"rawText": "Access remote machine",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Access remote machine",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 170,
			"versionNonce": 525819415,
			"isDeleted": false,
			"id": "qozVLxor0_3S0FSnbeiI7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -111.63702308160039,
			"y": -98.73615597162922,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 143.24813911948002,
			"height": 45.99206095760695,
			"seed": 337151031,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485806185,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": 0.852030875194356,
				"gap": 13.053470119578435
			},
			"endBinding": {
				"elementId": "jYo7Rnys",
				"focus": 0.0694675514382133,
				"gap": 8.419810674437144
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
					-143.24813911948002,
					-45.99206095760695
				]
			]
		},
		{
			"type": "text",
			"version": 130,
			"versionNonce": 1016682137,
			"isDeleted": false,
			"id": "BRJFI3LA",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -680.5919573178958,
			"y": -378.6533040919705,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 295.23968505859375,
			"height": 75,
			"seed": 1171184695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "83U6Q1SpjVBLa1ptikmtL",
					"type": "arrow"
				}
			],
			"updated": 1727485649181,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "ssh -l user <remote-server-ip>\n                ||\nssh user@<remote-server-ip>",
			"rawText": "ssh -l user <remote-server-ip>\n                ||\nssh user@<remote-server-ip>",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ssh -l user <remote-server-ip>\n                ||\nssh user@<remote-server-ip>",
			"lineHeight": 1.25,
			"baseline": 67
		},
		{
			"type": "arrow",
			"version": 152,
			"versionNonce": 1384776791,
			"isDeleted": false,
			"id": "83U6Q1SpjVBLa1ptikmtL",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -371.75490347713946,
			"y": -197.71563371213716,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 134.3317922556833,
			"height": 92.25053094344861,
			"seed": 489810263,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485806186,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "jYo7Rnys",
				"focus": -0.06175119925699961,
				"gap": 9.567606108463849
			},
			"endBinding": {
				"elementId": "BRJFI3LA",
				"focus": 0.23563439898047558,
				"gap": 13.687139436384712
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
					-134.3317922556833,
					-92.25053094344861
				]
			]
		},
		{
			"type": "text",
			"version": 434,
			"versionNonce": 188145815,
			"isDeleted": false,
			"id": "85eOM8Pg",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 380.2647923704542,
			"y": 400.34411359653535,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 820.3992919921875,
			"height": 200,
			"seed": 1792153913,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "mztYY1Dx3tx7kDpQySWR5",
					"type": "arrow"
				},
				{
					"id": "mjpkeNHbh70jtwKIox3gp",
					"type": "arrow"
				}
			],
			"updated": 1727486209214,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "ssh-copy-id -i public/key/path user@<remote-server-ip>\n\n                        ||\ncat ~/.ssh/id_rsa.pub | ssh kakaroto@192.168.1.3 'cat >> ~/.ssh/authorized_keys'\n\n                        ||\n\nscp /file/path user@server:/path/directory",
			"rawText": "ssh-copy-id -i public/key/path user@<remote-server-ip>\n\n                        ||\ncat ~/.ssh/id_rsa.pub | ssh kakaroto@192.168.1.3 'cat >> ~/.ssh/authorized_keys'\n\n                        ||\n\nscp /file/path user@server:/path/directory",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "ssh-copy-id -i public/key/path user@<remote-server-ip>\n\n                        ||\ncat ~/.ssh/id_rsa.pub | ssh kakaroto@192.168.1.3 'cat >> ~/.ssh/authorized_keys'\n\n                        ||\n\nscp /file/path user@server:/path/directory",
			"lineHeight": 1.25,
			"baseline": 192
		},
		{
			"type": "arrow",
			"version": 206,
			"versionNonce": 1748128441,
			"isDeleted": false,
			"id": "mztYY1Dx3tx7kDpQySWR5",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -58.47878207303439,
			"y": -34.964692293513565,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 198.65539938338185,
			"height": 279.73449241529784,
			"seed": 1077021849,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485871405,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.16649978710935567,
				"gap": 5.717993558537216
			},
			"endBinding": {
				"elementId": "Ey27FIiy",
				"focus": -0.35226246990245674,
				"gap": 15.924439192849206
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
					198.65539938338185,
					279.73449241529784
				]
			]
		},
		{
			"type": "text",
			"version": 99,
			"versionNonce": 398824215,
			"isDeleted": false,
			"id": "kXu8CRVt",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -382.5733637650666,
			"y": 80.57567097405177,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 174.94393920898438,
			"height": 35,
			"seed": 481399641,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "GckQlyVSXVhulanMopHrx",
					"type": "arrow"
				},
				{
					"id": "I2DGBXfe8bv2hQyyccJZE",
					"type": "arrow"
				}
			],
			"updated": 1727485878122,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Create Alias",
			"rawText": "Create Alias",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Create Alias",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 210,
			"versionNonce": 989630391,
			"isDeleted": false,
			"id": "GckQlyVSXVhulanMopHrx",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -96.42459379090305,
			"y": -36.06611667597963,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 165.63663604915996,
			"height": 101.66508637769948,
			"seed": 6549369,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485880031,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.5012173183794925,
				"gap": 4.6165691760711525
			},
			"endBinding": {
				"elementId": "kXu8CRVt",
				"focus": -0.17133551339774886,
				"gap": 14.976701272331923
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
					-165.63663604915996,
					101.66508637769948
				]
			]
		},
		{
			"type": "text",
			"version": 152,
			"versionNonce": 1292790009,
			"isDeleted": false,
			"id": "Pgez5puV",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -506.47379620268487,
			"y": 240.58385323241993,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 244.9198455810547,
			"height": 175,
			"seed": 1927311287,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "I2DGBXfe8bv2hQyyccJZE",
					"type": "arrow"
				}
			],
			"updated": 1727485823762,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "vim ~/.ssh/config\n\nfile content:\n\nHost snakecave\n    HostName 192.168.1.3\n    User kakaroto",
			"rawText": "vim ~/.ssh/config\n\nfile content:\n\nHost snakecave\n    HostName 192.168.1.3\n    User kakaroto",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "vim ~/.ssh/config\n\nfile content:\n\nHost snakecave\n    HostName 192.168.1.3\n    User kakaroto",
			"lineHeight": 1.25,
			"baseline": 167
		},
		{
			"type": "text",
			"version": 57,
			"versionNonce": 1870903481,
			"isDeleted": false,
			"id": "uzPS1M4g",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 317.2491817222125,
			"y": -80.85392617894905,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 195.27188110351562,
			"height": 35,
			"seed": 1744654967,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "Oo9U_j-DKabqZucK3GdzZ",
					"type": "arrow"
				}
			],
			"updated": 1727485803135,
			"link": "obsidian://open?vault=Brain&file=Knowledge%2FTechnology%2FComputing%2FShell%2FContent%2FSSH%2FContent%2FSSH",
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Additional info",
			"rawText": "Additional info",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Additional info",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 89,
			"versionNonce": 1324719737,
			"isDeleted": false,
			"id": "Oo9U_j-DKabqZucK3GdzZ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -43.06632216488924,
			"y": -61.17700843682016,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 346.3541068282781,
			"height": 0.19630606492687974,
			"seed": 1992226487,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485803135,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": 0.09634640350081228,
				"gap": 11.688194436673257
			},
			"endBinding": {
				"elementId": "uzPS1M4g",
				"focus": -0.10921810275023863,
				"gap": 13.96139705882365
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
					346.3541068282781,
					-0.19630606492687974
				]
			]
		},
		{
			"type": "text",
			"version": 78,
			"versionNonce": 453934999,
			"isDeleted": false,
			"id": "JSUMzHeT",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 514.14310262065,
			"y": 17.771903181115363,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 495.6277770996094,
			"height": 70,
			"seed": 236596439,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "jgj7SqJfn1O1EpJtndtMC",
					"type": "arrow"
				}
			],
			"updated": 1727486275676,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Check content inside remote server \n(from host machine)",
			"rawText": "Check content inside remote server \n(from host machine)",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Check content inside remote server \n(from host machine)",
			"lineHeight": 1.25,
			"baseline": 60
		},
		{
			"type": "arrow",
			"version": 35,
			"versionNonce": 151438807,
			"isDeleted": false,
			"id": "jgj7SqJfn1O1EpJtndtMC",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -46.259999880116396,
			"y": -51.13823631413561,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 547.7227783203125,
			"height": 94.70721935638655,
			"seed": 46380471,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486275677,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": 0.17706340538968057,
				"gap": 8.494516721446104
			},
			"endBinding": {
				"elementId": "JSUMzHeT",
				"focus": -0.460365976228648,
				"gap": 12.680324180453795
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
					547.7227783203125,
					94.70721935638655
				]
			]
		},
		{
			"type": "arrow",
			"version": 69,
			"versionNonce": 1587793815,
			"isDeleted": false,
			"id": "I2DGBXfe8bv2hQyyccJZE",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -331.4421801732087,
			"y": 122.30729998143727,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 65.53972914281559,
			"height": 97.37284342447924,
			"seed": 902822487,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485878122,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "kXu8CRVt",
				"focus": 0.20426183801259992,
				"gap": 6.731629007385493
			},
			"endBinding": {
				"elementId": "Pgez5puV",
				"focus": -0.47383689010078683,
				"gap": 20.903709826503416
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
					-65.53972914281559,
					97.37284342447924
				]
			]
		},
		{
			"type": "text",
			"version": 105,
			"versionNonce": 1916163065,
			"isDeleted": false,
			"id": "BhfgxNul",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 317.93901756094726,
			"y": 152.94025168442528,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 246.7078857421875,
			"height": 35,
			"seed": 360066455,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "kyD34Xn-CzZlquXjI5wNf",
					"type": "arrow"
				},
				{
					"id": "dd6aj8-mbvRijCA_AQZP_",
					"type": "arrow"
				}
			],
			"updated": 1727485868456,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Generate new Key",
			"rawText": "Generate new Key",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Generate new Key",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 444,
			"versionNonce": 1350001239,
			"isDeleted": false,
			"id": "dd6aj8-mbvRijCA_AQZP_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 517.5488901332515,
			"y": 197.33786681600424,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 156.8000568266193,
			"height": 39.12256633124048,
			"seed": 16521431,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727485874838,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "BhfgxNul",
				"focus": 0.17621199414027802,
				"gap": 9.39761513157896
			},
			"endBinding": {
				"elementId": "NUKmDh4u",
				"focus": -0.11565704172370488,
				"gap": 9.87987290912747
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
					156.8000568266193,
					39.12256633124048
				]
			]
		},
		{
			"type": "text",
			"version": 28,
			"versionNonce": 661945593,
			"isDeleted": false,
			"id": "Ey27FIiy",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 42.60410802147362,
			"y": 260.6942393146335,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 388.079833984375,
			"height": 35,
			"seed": 196536217,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "mztYY1Dx3tx7kDpQySWR5",
					"type": "arrow"
				},
				{
					"id": "mjpkeNHbh70jtwKIox3gp",
					"type": "arrow"
				}
			],
			"updated": 1727485871405,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Send key to remote machine:",
			"rawText": "Send key to remote machine:",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Send key to remote machine:",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 287,
			"versionNonce": 21685975,
			"isDeleted": false,
			"id": "mjpkeNHbh70jtwKIox3gp",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 244.04650291217945,
			"y": 309.7009724560809,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 147.1731958738057,
			"height": 77.46499063749695,
			"seed": 674342423,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486209215,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "Ey27FIiy",
				"focus": 0.2307918819712274,
				"gap": 14.006733141447398
			},
			"endBinding": {
				"elementId": "85eOM8Pg",
				"focus": -0.3069401309968108,
				"gap": 13.178150502957635
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
					147.1731958738057,
					77.46499063749695
				]
			]
		},
		{
			"type": "text",
			"version": 25,
			"versionNonce": 513143257,
			"isDeleted": false,
			"id": "5oH11oaJ",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -164.61657143075615,
			"y": 403.74910078973716,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 140.0839385986328,
			"height": 35,
			"seed": 1984060695,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "RE0TKQq9_ewvWMwjgolW7",
					"type": "arrow"
				},
				{
					"id": "_fpoypfZdyGRgdeAu4HwI",
					"type": "arrow"
				}
			],
			"updated": 1727486738321,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "SSH Agent",
			"rawText": "SSH Agent",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "SSH Agent",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 65,
			"versionNonce": 1438716791,
			"isDeleted": false,
			"id": "RE0TKQq9_ewvWMwjgolW7",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -81.83127510032055,
			"y": -31.38599035609633,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 10.329599135703049,
			"height": 419.92055257161473,
			"seed": 201203065,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486230990,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.1674089323705139,
				"gap": 9.296695495954452
			},
			"endBinding": {
				"elementId": "5oH11oaJ",
				"focus": 0.022831404507758953,
				"gap": 15.21453857421875
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
					-10.329599135703049,
					419.92055257161473
				]
			]
		},
		{
			"type": "text",
			"version": 108,
			"versionNonce": 1117148761,
			"isDeleted": false,
			"id": "POiyW7CU",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 857.7989966030981,
			"y": -207.57419226039337,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 273.8197326660156,
			"height": 25,
			"seed": 474183993,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "vIBsl5C9PCQ_X1Dt0Nhzf",
					"type": "arrow"
				}
			],
			"updated": 1727486288177,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "sudo systemctl restart ssh",
			"rawText": "sudo systemctl restart ssh",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "sudo systemctl restart ssh",
			"lineHeight": 1.25,
			"baseline": 17
		},
		{
			"type": "text",
			"version": 76,
			"versionNonce": 1289990393,
			"isDeleted": false,
			"id": "v9HcsL9e",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 442.4423478400771,
			"y": -192.7952921139091,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 282.04388427734375,
			"height": 35,
			"seed": 1124000215,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "KYsAFD1QfiJ7uQzco7MN_",
					"type": "arrow"
				},
				{
					"id": "vIBsl5C9PCQ_X1Dt0Nhzf",
					"type": "arrow"
				}
			],
			"updated": 1727486287119,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Restart SSH service",
			"rawText": "Restart SSH service",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Restart SSH service",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 47,
			"versionNonce": 1169034263,
			"isDeleted": false,
			"id": "KYsAFD1QfiJ7uQzco7MN_",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -42.90036456226676,
			"y": -83.25086869268512,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 479.25710042317735,
			"height": 86.72271728515625,
			"seed": 1946081209,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486283574,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.4306357821753487,
				"gap": 11.854152039295741
			},
			"endBinding": {
				"elementId": "v9HcsL9e",
				"focus": 0.4950864713181313,
				"gap": 6.085611979166515
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
					479.25710042317735,
					-86.72271728515625
				]
			]
		},
		{
			"type": "arrow",
			"version": 63,
			"versionNonce": 250958873,
			"isDeleted": false,
			"id": "vIBsl5C9PCQ_X1Dt0Nhzf",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 734.5612850145563,
			"y": -171.4052791161992,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 115.63049316406284,
			"height": 19.705377071683387,
			"seed": 428683863,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486288177,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "v9HcsL9e",
				"focus": 0.7250672433661965,
				"gap": 10.075052897135492
			},
			"endBinding": {
				"elementId": "POiyW7CU",
				"focus": 0.5767121948377733,
				"gap": 7.607218424479186
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
					115.63049316406284,
					-19.705377071683387
				]
			]
		},
		{
			"type": "text",
			"version": 63,
			"versionNonce": 2011273113,
			"isDeleted": false,
			"id": "nRBdutVv",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -26.16452471851653,
			"y": -465.5709167070079,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 533.81982421875,
			"height": 35,
			"seed": 1451221465,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "ayecR-x0MpEBLp8QGzMWK",
					"type": "arrow"
				},
				{
					"id": "CTGnq_KJzYh-lKR7AWNQr",
					"type": "arrow"
				}
			],
			"updated": 1727486622850,
			"link": null,
			"locked": false,
			"fontSize": 28,
			"fontFamily": 1,
			"text": "Check if daemon allows public key auth",
			"rawText": "Check if daemon allows public key auth",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "Check if daemon allows public key auth",
			"lineHeight": 1.25,
			"baseline": 25
		},
		{
			"type": "arrow",
			"version": 36,
			"versionNonce": 315248247,
			"isDeleted": false,
			"id": "ayecR-x0MpEBLp8QGzMWK",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": -83.97966957528752,
			"y": -99.98686112432551,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 292.1187337239585,
			"height": 319.50480143229174,
			"seed": 333914361,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486565749,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "mtcNJo8a",
				"focus": -0.5931694272772382,
				"gap": 14.304175272274733
			},
			"endBinding": {
				"elementId": "nRBdutVv",
				"focus": 0.022893203447111,
				"gap": 11.079254150390625
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
					292.1187337239585,
					-319.50480143229174
				]
			]
		},
		{
			"type": "text",
			"version": 307,
			"versionNonce": 1951242903,
			"isDeleted": false,
			"id": "IsiPoUIB",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 751.4355729377332,
			"y": -481.055378635867,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 397.1995849609375,
			"height": 150,
			"seed": 184954425,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"boundElements": [
				{
					"id": "CTGnq_KJzYh-lKR7AWNQr",
					"type": "arrow"
				}
			],
			"updated": 1727486638944,
			"link": null,
			"locked": false,
			"fontSize": 20,
			"fontFamily": 1,
			"text": "/etc/ssh/sshd_config\n\ncontent:\n \nPublicAuthentication yes\nAuthorizedKeysFile .ssh/authorized_keys",
			"rawText": "/etc/ssh/sshd_config\n\ncontent:\n \nPublicAuthentication yes\nAuthorizedKeysFile .ssh/authorized_keys",
			"textAlign": "left",
			"verticalAlign": "top",
			"containerId": null,
			"originalText": "/etc/ssh/sshd_config\n\ncontent:\n \nPublicAuthentication yes\nAuthorizedKeysFile .ssh/authorized_keys",
			"lineHeight": 1.25,
			"baseline": 142
		},
		{
			"type": "arrow",
			"version": 289,
			"versionNonce": 192618711,
			"isDeleted": false,
			"id": "CTGnq_KJzYh-lKR7AWNQr",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"angle": 0,
			"x": 509.4847511780249,
			"y": -423.6366059115261,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"width": 215.03340232611447,
			"height": 18.543907799087947,
			"seed": 2134842295,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"boundElements": [],
			"updated": 1727486638944,
			"link": null,
			"locked": false,
			"startBinding": {
				"elementId": "nRBdutVv",
				"focus": 0.07174563023244165,
				"gap": 7.171579996744754
			},
			"endBinding": {
				"elementId": "IsiPoUIB",
				"focus": -0.22155010820746776,
				"gap": 26.917419433593864
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
					215.03340232611447,
					18.543907799087947
				]
			]
		},
		{
			"id": "vKVfcAOp",
			"type": "text",
			"x": -607.463714531603,
			"y": 489.6791297761441,
			"width": 275.2997741699219,
			"height": 125,
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
			"seed": 1227626263,
			"version": 152,
			"versionNonce": 2006171639,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "_fpoypfZdyGRgdeAu4HwI",
					"type": "arrow"
				}
			],
			"updated": 1727486739883,
			"link": null,
			"locked": false,
			"text": "SSH Agent not running\n\n$ eval \"$(ssh-agent -s)\"\n$ ssh-add private/key/path\n$ssh-add -l",
			"rawText": "SSH Agent not running\n\n$ eval \"$(ssh-agent -s)\"\n$ ssh-add private/key/path\n$ssh-add -l",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 117,
			"containerId": null,
			"originalText": "SSH Agent not running\n\n$ eval \"$(ssh-agent -s)\"\n$ ssh-add private/key/path\n$ssh-add -l",
			"lineHeight": 1.25
		},
		{
			"id": "_fpoypfZdyGRgdeAu4HwI",
			"type": "arrow",
			"x": -135.2591848697445,
			"y": 446.52533227969525,
			"width": 180.30702156082867,
			"height": 65.02014686314914,
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
			"seed": 692760791,
			"version": 120,
			"versionNonce": 1052732983,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1727486739883,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-180.30702156082867,
					65.02014686314914
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "5oH11oaJ",
				"focus": -0.25625188489058215,
				"gap": 7.776231489958093
			},
			"endBinding": {
				"elementId": "vKVfcAOp",
				"focus": 0.13366848440122667,
				"gap": 16.597733931107996
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
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
		"scrollX": 1031.6634881466605,
		"scrollY": 728.8997914552127,
		"zoom": {
			"value": 0.55
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