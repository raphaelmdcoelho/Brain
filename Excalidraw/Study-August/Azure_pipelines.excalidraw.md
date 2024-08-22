---

excalidraw-plugin: parsed
tags: [excalidraw]

---
==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠==


# Text Elements
Azure Pipelines ^IkM6GrN9

Deployment groups ^oxroOeVu

Agents ^bNAXFi1G

Pipelines ^jhxSeelf

Types of agents

- Microsoft-hosted
- Self-hosted
- Azure VM Scale Set ^XI7u8VUF

It is a computing infrastructure with
 installed agent software that runs
 one job at a time ^mKjjy3sF

Specifies jobs in your pipeline ^QCKbIw5q

Every pipeline has at least one job ^tCTWZf4i

A job is a series of steps that
 run sequentially as a unit or in
 other words, it is a smallest unit
 of work that can be schedule to run ^oHFTOSre

Trigger ^FAkm0mfF

Pipeline ^x7daTO3z

Stage ^twqhnzLL

Stage ^eGAx8HOH

Environment ^VcjJaQj5

Agent ^OfTXLyqd

Job ^EacOcC8O

Agent ^6CdT3ypi

Job ^dojzPjCX

Stage ^N1lkc7b7

Steps ^Jz823fMH

Step: Script ^HetWugJ6

Step: Task ^U2iYMFQs

Key concepts overview ^3lSQUBbC

It is a prepackaged script ^JuCjPrBF

Publish build Artifact ^k66aFm2Q

run ^5FmeHYLR

A Artifact is a collection
of files or packages published by a run ^n6elMGvQ

Job ^zDKc2f0u

trigger:
- main

pool:
    vmImage: 'ubuntu-latest'

steps:
- task: TaskName@1
  inputs:
    option : 'value'
 ^G1PAGSuq

Deployment group jobs ^Rv5wZLKc

Agent job ^0LbBQSy8

Examples ^Uh7DPV3E

strategy:
    matrix:
        linux:
            imageName: "..."
    ...
    maxParallel: 3

pool: $(imageName) ^bLFOKM8i

jobs:
- job: Name
  dependsOn: JobName
  condition: failed()
  steps:
  - script: echo Hello
  - bash: |
        echo Hello
    env:
      NAME: $(System.TeamProject)
    displayName: 'Name' ^W4DXxTOZ

%%
# Drawing
```json
{
	"type": "excalidraw",
	"version": 2,
	"source": "https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/1.9.28",
	"elements": [
		{
			"id": "IkM6GrN9",
			"type": "text",
			"x": -483.105339984315,
			"y": -131.9513860241168,
			"width": 459.9248860177459,
			"height": 79.49480084610828,
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
			"seed": 681720744,
			"version": 229,
			"versionNonce": 692529320,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "y6szClVSIO9m0tsHoDLFn",
					"type": "arrow"
				},
				{
					"id": "DHK-mKUAvBg6QsaB-Wx2m",
					"type": "arrow"
				},
				{
					"id": "0_ZID_o_-bVhmAeJiyrOM",
					"type": "arrow"
				}
			],
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "Azure Pipelines",
			"rawText": "Azure Pipelines",
			"fontSize": 63.595840676886624,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 56,
			"containerId": null,
			"originalText": "Azure Pipelines",
			"lineHeight": 1.25
		},
		{
			"id": "oxroOeVu",
			"type": "text",
			"x": 390.7504396285565,
			"y": 10.104829526439858,
			"width": 249.39588928222656,
			"height": 35,
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
			"seed": 2006619304,
			"version": 430,
			"versionNonce": 870567592,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "y6szClVSIO9m0tsHoDLFn",
					"type": "arrow"
				}
			],
			"updated": 1724273073145,
			"link": null,
			"locked": false,
			"text": "Deployment groups",
			"rawText": "Deployment groups",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": "Deployment groups",
			"lineHeight": 1.25
		},
		{
			"id": "y6szClVSIO9m0tsHoDLFn",
			"type": "arrow",
			"x": -12.173425005487898,
			"y": -64.90295817999355,
			"width": 447.95845496798825,
			"height": 64.14781828875033,
			"angle": 0.034188135853168156,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1050968232,
			"version": 1117,
			"versionNonce": 1819165864,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273073145,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					447.95845496798825,
					64.14781828875033
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "IkM6GrN9",
				"focus": -0.30246140676723127,
				"gap": 12.229029051712928
			},
			"endBinding": {
				"elementId": "oxroOeVu",
				"focus": 0.15861879252297462,
				"gap": 3.2227714033529082
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "bNAXFi1G",
			"type": "text",
			"x": 86.03055004804548,
			"y": 164.2836364831087,
			"width": 65.57994079589844,
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
			"seed": 1234042792,
			"version": 159,
			"versionNonce": 1164614360,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "DHK-mKUAvBg6QsaB-Wx2m",
					"type": "arrow"
				},
				{
					"id": "JKnrkEEP7HAugg3L26bFi",
					"type": "arrow"
				},
				{
					"id": "pRa8mfDsTYq1Wldyd_cGb",
					"type": "arrow"
				}
			],
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "Agents",
			"rawText": "Agents",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Agents",
			"lineHeight": 1.25
		},
		{
			"id": "DHK-mKUAvBg6QsaB-Wx2m",
			"type": "arrow",
			"x": -80.49691770497225,
			"y": -46.614964702635994,
			"width": 158.2012325344936,
			"height": 210.74485097415433,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1095947992,
			"version": 615,
			"versionNonce": 272834216,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					158.2012325344936,
					210.74485097415433
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "IkM6GrN9",
				"focus": -0.5328076513096273,
				"gap": 5.8416204753725225
			},
			"endBinding": {
				"elementId": "bNAXFi1G",
				"focus": -0.7496979153214699,
				"gap": 8.327654654328278
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "jhxSeelf",
			"type": "text",
			"x": -564.8440197081966,
			"y": 145.5028208366594,
			"width": 110.8519287109375,
			"height": 35,
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
			"seed": 1882746072,
			"version": 103,
			"versionNonce": 2082445016,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "oPNgVTQ3IVxEreD950zqC",
					"type": "arrow"
				},
				{
					"id": "vr7JjT6yMWwcYJ28bAUIw",
					"type": "arrow"
				},
				{
					"id": "0_ZID_o_-bVhmAeJiyrOM",
					"type": "arrow"
				},
				{
					"id": "xsMEQO44DSwf7E4JiXhVn",
					"type": "arrow"
				},
				{
					"id": "6YkxYoOkslY5ya9c57Qyc",
					"type": "arrow"
				}
			],
			"updated": 1724273083238,
			"link": null,
			"locked": false,
			"text": "Pipelines",
			"rawText": "Pipelines",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": "Pipelines",
			"lineHeight": 1.25
		},
		{
			"id": "XI7u8VUF",
			"type": "text",
			"x": 402.02517388331137,
			"y": 332.3430746697177,
			"width": 215.47984313964844,
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
			"seed": 588646312,
			"version": 327,
			"versionNonce": 635138472,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "JKnrkEEP7HAugg3L26bFi",
					"type": "arrow"
				}
			],
			"updated": 1724273071680,
			"link": null,
			"locked": false,
			"text": "Types of agents\n\n- Microsoft-hosted\n- Self-hosted\n- Azure VM Scale Set",
			"rawText": "Types of agents\n\n- Microsoft-hosted\n- Self-hosted\n- Azure VM Scale Set",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 117,
			"containerId": null,
			"originalText": "Types of agents\n\n- Microsoft-hosted\n- Self-hosted\n- Azure VM Scale Set",
			"lineHeight": 1.25
		},
		{
			"id": "JKnrkEEP7HAugg3L26bFi",
			"type": "arrow",
			"x": 158.26924223336263,
			"y": 190.36730566858245,
			"width": 231.63169509345775,
			"height": 130.08635357232237,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 782325416,
			"version": 422,
			"versionNonce": 152643496,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273071680,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					231.63169509345775,
					130.08635357232237
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "bNAXFi1G",
				"focus": -0.2730194471520877,
				"gap": 6.7463552359500625
			},
			"endBinding": {
				"elementId": "XI7u8VUF",
				"focus": 0.05749781892700671,
				"gap": 16.981027981740283
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "pRa8mfDsTYq1Wldyd_cGb",
			"type": "arrow",
			"x": 110.91450588958254,
			"y": 197.95189198572757,
			"width": 238.17809812672772,
			"height": 299.5684258373351,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 603569576,
			"version": 845,
			"versionNonce": 1100222424,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273069103,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					238.17809812672772,
					299.5684258373351
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "bNAXFi1G",
				"focus": 0.5783365519880441,
				"gap": 8.668255502618877
			},
			"endBinding": {
				"elementId": "mKjjy3sF",
				"focus": -0.030371716154311848,
				"gap": 13.731247268009184
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "mKjjy3sF",
			"type": "text",
			"x": 212.17372866483532,
			"y": 511.2515650910719,
			"width": 368.2996520996094,
			"height": 75,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"e5VkQMd3SEHNbzctd54_t"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1125284520,
			"version": 592,
			"versionNonce": 1922147800,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "pRa8mfDsTYq1Wldyd_cGb",
					"type": "arrow"
				}
			],
			"updated": 1724273069103,
			"link": null,
			"locked": false,
			"text": "It is a computing infrastructure with\n installed agent software that runs\n one job at a time",
			"rawText": "It is a computing infrastructure with\n installed agent software that runs\n one job at a time",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 67,
			"containerId": null,
			"originalText": "It is a computing infrastructure with\n installed agent software that runs\n one job at a time",
			"lineHeight": 1.25
		},
		{
			"id": "PYuLd5I1a67d1CzMsi4bD",
			"type": "freedraw",
			"x": 217.9476629139332,
			"y": 578.6392877716136,
			"width": 184.7709431632819,
			"height": 5.6332696487239104,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 30,
			"groupIds": [
				"e5VkQMd3SEHNbzctd54_t"
			],
			"frameId": null,
			"roundness": null,
			"seed": 990578392,
			"version": 295,
			"versionNonce": 1630819544,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273069103,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.1266539297448617
				],
				[
					1.126616265387156,
					-1.1266539297448617
				],
				[
					2.253307859489553,
					-1.1266539297448617
				],
				[
					4.506615718979106,
					-1.1266539297448617
				],
				[
					6.759923578468658,
					-1.1266539297448617
				],
				[
					9.013231437958154,
					-2.2533078594896097
				],
				[
					11.266539297447707,
					-2.2533078594896097
				],
				[
					13.51984715693726,
					-1.1266539297448617
				],
				[
					15.773155016426813,
					-1.1266539297448617
				],
				[
					19.15307914130352,
					-1.1266539297448617
				],
				[
					21.406387000793075,
					-2.2533078594896097
				],
				[
					23.659694860282627,
					-2.2533078594896097
				],
				[
					25.91300271977218,
					-2.2533078594896097
				],
				[
					28.166310579261733,
					-2.2533078594896097
				],
				[
					29.292926844648832,
					-2.2533078594896097
				],
				[
					31.546234704138385,
					-2.2533078594896097
				],
				[
					33.79954256362794,
					-2.2533078594896097
				],
				[
					36.05285042311749,
					-2.2533078594896097
				],
				[
					37.17954201721989,
					-2.2533078594896097
				],
				[
					40.559466142096596,
					-3.3799617892343576
				],
				[
					42.81277400158615,
					-4.5066157189791625
				],
				[
					45.0660818610757,
					-4.5066157189791625
				],
				[
					47.319389720565255,
					-4.5066157189791625
				],
				[
					50.69931384544191,
					-4.5066157189791625
				],
				[
					52.95262170493146,
					-4.5066157189791625
				],
				[
					56.33262115852341,
					-4.5066157189791625
				],
				[
					58.58592901801296,
					-4.5066157189791625
				],
				[
					60.839236877502515,
					-4.5066157189791625
				],
				[
					63.09254473699207,
					-4.5066157189791625
				],
				[
					66.47246886186878,
					-3.3799617892343576
				],
				[
					69.85239298674543,
					-2.2533078594896097
				],
				[
					72.10570084623498,
					-2.2533078594896097
				],
				[
					75.48570029982693,
					-2.2533078594896097
				],
				[
					77.73900815931648,
					-2.2533078594896097
				],
				[
					81.11893228419319,
					-2.2533078594896097
				],
				[
					84.49893173778514,
					-2.2533078594896097
				],
				[
					87.87885586266185,
					-2.2533078594896097
				],
				[
					90.1321637221514,
					-3.3799617892343576
				],
				[
					93.51208784702806,
					-4.5066157189791625
				],
				[
					95.76539570651761,
					-4.5066157189791625
				],
				[
					99.14539516010956,
					-4.5066157189791625
				],
				[
					102.52531928498627,
					-4.5066157189791625
				],
				[
					104.77862714447582,
					-3.3799617892343576
				],
				[
					107.03193500396537,
					-4.5066157189791625
				],
				[
					110.41193445755732,
					-4.5066157189791625
				],
				[
					113.79185858243403,
					-4.5066157189791625
				],
				[
					117.17178270731068,
					-4.5066157189791625
				],
				[
					120.55178216090263,
					-4.5066157189791625
				],
				[
					123.93170628577934,
					-4.5066157189791625
				],
				[
					126.1850141452689,
					-5.6332696487239104
				],
				[
					129.56501359886084,
					-5.6332696487239104
				],
				[
					131.8183214583504,
					-5.6332696487239104
				],
				[
					134.07162931783995,
					-5.6332696487239104
				],
				[
					136.3249371773295,
					-5.6332696487239104
				],
				[
					139.70486130220615,
					-5.6332696487239104
				],
				[
					140.8314775675933,
					-5.6332696487239104
				],
				[
					143.08478542708292,
					-5.6332696487239104
				],
				[
					146.46478488067487,
					-4.5066157189791625
				],
				[
					149.84470900555152,
					-4.5066157189791625
				],
				[
					153.22470845914347,
					-4.5066157189791625
				],
				[
					155.47801631863297,
					-4.5066157189791625
				],
				[
					157.73132417812258,
					-4.5066157189791625
				],
				[
					159.98463203761207,
					-3.3799617892343576
				],
				[
					163.36455616248884,
					-3.3799617892343576
				],
				[
					166.7444802873655,
					-3.3799617892343576
				],
				[
					168.997788146855,
					-3.3799617892343576
				],
				[
					171.2510960063446,
					-3.3799617892343576
				],
				[
					173.5044038658341,
					-3.3799617892343576
				],
				[
					175.7577117253237,
					-3.3799617892343576
				],
				[
					178.0110195848132,
					-3.3799617892343576
				],
				[
					180.2643274443028,
					-3.3799617892343576
				],
				[
					181.39101903840515,
					-3.3799617892343576
				],
				[
					182.5176353037923,
					-3.3799617892343576
				],
				[
					184.7709431632819,
					-3.3799617892343576
				],
				[
					184.7709431632819,
					-2.2533078594896097
				],
				[
					182.5176353037923,
					-1.1266539297448617
				],
				[
					182.5176353037923,
					-1.1266539297448617
				]
			],
			"pressures": [
				0.109375,
				0.1845703125,
				0.3837890625,
				0.466796875,
				0.5009765625,
				0.51171875,
				0.513671875,
				0.51953125,
				0.52734375,
				0.5302734375,
				0.5361328125,
				0.5390625,
				0.5400390625,
				0.541015625,
				0.546875,
				0.546875,
				0.5556640625,
				0.5625,
				0.564453125,
				0.5654296875,
				0.568359375,
				0.568359375,
				0.568359375,
				0.5673828125,
				0.5693359375,
				0.5703125,
				0.5712890625,
				0.5732421875,
				0.572265625,
				0.5732421875,
				0.576171875,
				0.576171875,
				0.5771484375,
				0.5791015625,
				0.5791015625,
				0.58203125,
				0.5830078125,
				0.5849609375,
				0.5859375,
				0.5869140625,
				0.5869140625,
				0.5859375,
				0.5859375,
				0.5869140625,
				0.587890625,
				0.595703125,
				0.5966796875,
				0.595703125,
				0.5927734375,
				0.59375,
				0.603515625,
				0.6083984375,
				0.609375,
				0.6103515625,
				0.6103515625,
				0.611328125,
				0.611328125,
				0.6103515625,
				0.61328125,
				0.609375,
				0.6083984375,
				0.609375,
				0.6103515625,
				0.6083984375,
				0.609375,
				0.609375,
				0.6142578125,
				0.615234375,
				0.6171875,
				0.6171875,
				0.615234375,
				0.6142578125,
				0.615234375,
				0.6162109375,
				0.6162109375,
				0.5654296875,
				0.130859375,
				0
			],
			"simulatePressure": false,
			"lastCommittedPoint": [
				182.5176353037923,
				-1.1266539297448617
			]
		},
		{
			"id": "heLO209Njr_NLUrCntZ4C",
			"type": "freedraw",
			"x": 220.20097077342092,
			"y": 547.6563047036321,
			"width": 247.86348790027392,
			"height": 6.759923578468715,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 30,
			"groupIds": [
				"e5VkQMd3SEHNbzctd54_t"
			],
			"frameId": null,
			"roundness": null,
			"seed": 120024744,
			"version": 343,
			"versionNonce": 243530200,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273069103,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-1.126616265387156
				],
				[
					0,
					0
				],
				[
					1.1266915941023967,
					-1.126616265387156
				],
				[
					2.253307859489553,
					-1.126616265387156
				],
				[
					4.506615718979106,
					-1.126616265387156
				],
				[
					6.759923578468658,
					-1.126616265387156
				],
				[
					10.139923032060608,
					-1.126616265387156
				],
				[
					12.39323089155016,
					-1.126616265387156
				],
				[
					15.77315501642687,
					-1.126616265387156
				],
				[
					18.026462875916422,
					-1.126616265387156
				],
				[
					20.27977073540592,
					-1.126616265387156
				],
				[
					22.53307859489547,
					-1.126616265387156
				],
				[
					25.91300271977218,
					0
				],
				[
					28.166310579261733,
					1.1266915941024536
				],
				[
					30.419618438751286,
					1.1266915941024536
				],
				[
					32.67292629824084,
					0
				],
				[
					36.05292575183279,
					0
				],
				[
					37.179542017219944,
					0
				],
				[
					39.4328498767095,
					1.1266915941024536
				],
				[
					40.559541470811894,
					1.1266915941024536
				],
				[
					42.81277400158615,
					0
				],
				[
					46.1927734551781,
					0
				],
				[
					47.319389720565255,
					0
				],
				[
					49.57269758005481,
					1.1266915941024536
				],
				[
					50.699389174157204,
					1.1266915941024536
				],
				[
					52.95269703364676,
					1.1266915941024536
				],
				[
					55.20600489313631,
					1.1266915941024536
				],
				[
					57.45931275262586,
					2.2533078594896097
				],
				[
					59.712620612115415,
					3.3799994535919495
				],
				[
					61.96592847160497,
					3.3799994535919495
				],
				[
					63.09254473699207,
					3.3799994535919495
				],
				[
					66.47246886186878,
					3.3799994535919495
				],
				[
					68.72577672135839,
					3.3799994535919495
				],
				[
					69.85246831546073,
					3.3799994535919495
				],
				[
					72.10577617495034,
					4.506615718979106
				],
				[
					74.35908403443983,
					4.506615718979106
				],
				[
					76.61239189392933,
					3.3799994535919495
				],
				[
					78.86569975341894,
					3.3799994535919495
				],
				[
					81.11900761290843,
					3.3799994535919495
				],
				[
					83.37231547239804,
					2.2533078594896097
				],
				[
					85.62562333188754,
					3.3799994535919495
				],
				[
					87.87893119137715,
					2.2533078594896097
				],
				[
					91.2588553162538,
					2.2533078594896097
				],
				[
					93.51216317574341,
					2.2533078594896097
				],
				[
					95.7654710352329,
					2.2533078594896097
				],
				[
					99.14539516010956,
					2.2533078594896097
				],
				[
					101.39870301959917,
					2.2533078594896097
				],
				[
					105.90531873857827,
					2.2533078594896097
				],
				[
					108.15862659806777,
					2.2533078594896097
				],
				[
					111.53862605165972,
					2.2533078594896097
				],
				[
					113.79193391114933,
					2.2533078594896097
				],
				[
					118.29847430141314,
					1.1266915941024536
				],
				[
					121.67847375500509,
					1.1266915941024536
				],
				[
					123.93178161449458,
					0
				],
				[
					127.31170573937135,
					1.1266915941024536
				],
				[
					130.6917051929633,
					1.1266915941024536
				],
				[
					134.07162931783995,
					1.1266915941024536
				],
				[
					136.32493717732956,
					1.1266915941024536
				],
				[
					139.7048613022062,
					2.2533078594896097
				],
				[
					141.9581691616957,
					2.2533078594896097
				],
				[
					144.21147702118532,
					2.2533078594896097
				],
				[
					147.59147647477727,
					3.3799994535919495
				],
				[
					149.84478433426676,
					3.3799994535919495
				],
				[
					154.35140005324587,
					4.506615718979106
				],
				[
					157.73132417812263,
					4.506615718979106
				],
				[
					161.11132363171458,
					4.506615718979106
				],
				[
					164.49124775659124,
					4.506615718979106
				],
				[
					167.8711718814679,
					4.506615718979106
				],
				[
					172.377787600447,
					3.3799994535919495
				],
				[
					176.8844033194261,
					3.3799994535919495
				],
				[
					180.26440277301805,
					3.3799994535919495
				],
				[
					183.6443268978947,
					4.506615718979106
				],
				[
					187.02425102277147,
					4.506615718979106
				],
				[
					189.27755888226096,
					5.633307313081559
				],
				[
					192.6575583358529,
					4.506615718979106
				],
				[
					196.03748246072968,
					4.506615718979106
				],
				[
					199.41748191432163,
					4.506615718979106
				],
				[
					202.79740603919828,
					4.506615718979106
				],
				[
					206.17740549279023,
					3.3799994535919495
				],
				[
					210.68394588305404,
					2.2533078594896097
				],
				[
					215.19056160203314,
					2.2533078594896097
				],
				[
					218.5705610556251,
					1.1266915941024536
				],
				[
					221.95048518050186,
					1.1266915941024536
				],
				[
					224.20379303999135,
					1.1266915941024536
				],
				[
					227.5837924935833,
					1.1266915941024536
				],
				[
					229.8371003530728,
					1.1266915941024536
				],
				[
					232.0904082125624,
					1.1266915941024536
				],
				[
					233.21702447794956,
					1.1266915941024536
				],
				[
					235.47033233743906,
					1.1266915941024536
				],
				[
					237.72364019692867,
					1.1266915941024536
				],
				[
					239.97694805641817,
					1.1266915941024536
				],
				[
					242.23025591590778,
					2.2533078594896097
				],
				[
					243.35687218129493,
					1.1266915941024536
				],
				[
					245.61018004078443,
					1.1266915941024536
				],
				[
					246.73687163488688,
					1.1266915941024536
				],
				[
					247.86348790027392,
					1.1266915941024536
				],
				[
					245.61018004078443,
					2.2533078594896097
				],
				[
					245.61018004078443,
					2.2533078594896097
				]
			],
			"pressures": [
				0.0361328125,
				0.3330078125,
				0.376953125,
				0.466796875,
				0.474609375,
				0.48828125,
				0.498046875,
				0.5087890625,
				0.5166015625,
				0.51953125,
				0.5224609375,
				0.5263671875,
				0.5498046875,
				0.5595703125,
				0.5625,
				0.5654296875,
				0.56640625,
				0.568359375,
				0.568359375,
				0.568359375,
				0.5712890625,
				0.5732421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.5751953125,
				0.576171875,
				0.576171875,
				0.5751953125,
				0.580078125,
				0.5810546875,
				0.5810546875,
				0.58203125,
				0.5810546875,
				0.5810546875,
				0.5810546875,
				0.580078125,
				0.58203125,
				0.5830078125,
				0.58203125,
				0.5810546875,
				0.58203125,
				0.58203125,
				0.580078125,
				0.5771484375,
				0.578125,
				0.5810546875,
				0.58203125,
				0.5830078125,
				0.58203125,
				0.5849609375,
				0.5869140625,
				0.5830078125,
				0.5830078125,
				0.58203125,
				0.58203125,
				0.58203125,
				0.58203125,
				0.58203125,
				0.5810546875,
				0.580078125,
				0.5830078125,
				0.5859375,
				0.5849609375,
				0.5849609375,
				0.583984375,
				0.5830078125,
				0.58203125,
				0.58203125,
				0.5830078125,
				0.58203125,
				0.580078125,
				0.580078125,
				0.5810546875,
				0.5810546875,
				0.58203125,
				0.583984375,
				0.587890625,
				0.591796875,
				0.5947265625,
				0.6015625,
				0.6162109375,
				0.6201171875,
				0.6220703125,
				0.6240234375,
				0.625,
				0.6328125,
				0.638671875,
				0.640625,
				0.646484375,
				0.64453125,
				0.6455078125,
				0.646484375,
				0.646484375,
				0.6484375,
				0.6484375,
				0.6494140625,
				0.203125,
				0
			],
			"simulatePressure": false,
			"lastCommittedPoint": [
				245.61018004078443,
				2.2533078594896097
			]
		},
		{
			"id": "QCKbIw5q",
			"type": "text",
			"x": -1065.6903791321968,
			"y": 91.5134387415593,
			"width": 281.0397033691406,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 338615464,
			"version": 234,
			"versionNonce": 274705320,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "oPNgVTQ3IVxEreD950zqC",
					"type": "arrow"
				}
			],
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "Specifies jobs in your pipeline",
			"rawText": "Specifies jobs in your pipeline",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Specifies jobs in your pipeline",
			"lineHeight": 1.25
		},
		{
			"id": "oPNgVTQ3IVxEreD950zqC",
			"type": "arrow",
			"x": -569.1195368321017,
			"y": 149.50847489633642,
			"width": 202.63332583111344,
			"height": 31.815948954098474,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1536515752,
			"version": 492,
			"versionNonce": 1715777192,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273085444,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-202.63332583111344,
					-31.815948954098474
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jhxSeelf",
				"focus": 0.15725452285717342,
				"gap": 4.275517123905161
			},
			"endBinding": {
				"elementId": "QCKbIw5q",
				"focus": -0.3011683781636178,
				"gap": 12.89781309984096
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "tCTWZf4i",
			"type": "text",
			"x": -1073.2735507418183,
			"y": 23.042478302088284,
			"width": 347.39971923828125,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 882409432,
			"version": 249,
			"versionNonce": 29095592,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "6YkxYoOkslY5ya9c57Qyc",
					"type": "arrow"
				},
				{
					"id": "LKC2_Mxx6b_mEywNUxcsL",
					"type": "arrow"
				}
			],
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "Every pipeline has at least one job",
			"rawText": "Every pipeline has at least one job",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Every pipeline has at least one job",
			"lineHeight": 1.25
		},
		{
			"id": "6YkxYoOkslY5ya9c57Qyc",
			"type": "arrow",
			"x": -524.0628423894196,
			"y": 130.58592358410334,
			"width": 189.18734440985634,
			"height": 85.33620648101757,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 156368344,
			"version": 566,
			"versionNonce": 1759241688,
			"isDeleted": false,
			"boundElements": [],
			"updated": 1724273083447,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-189.18734440985634,
					-85.33620648101757
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jhxSeelf",
				"focus": 0.6073084034329906,
				"gap": 14.916897252556055
			},
			"endBinding": {
				"elementId": "tCTWZf4i",
				"focus": -0.8182380811236407,
				"gap": 12.623644704261096
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "oHFTOSre",
			"type": "text",
			"x": -1084.9664313259832,
			"y": -191.0297518416557,
			"width": 374.37969970703125,
			"height": 100,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1727193816,
			"version": 290,
			"versionNonce": 928440744,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "LKC2_Mxx6b_mEywNUxcsL",
					"type": "arrow"
				}
			],
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "A job is a series of steps that\n run sequentially as a unit or in\n other words, it is a smallest unit\n of work that can be schedule to run",
			"rawText": "A job is a series of steps that\n run sequentially as a unit or in\n other words, it is a smallest unit\n of work that can be schedule to run",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 92,
			"containerId": null,
			"originalText": "A job is a series of steps that\n run sequentially as a unit or in\n other words, it is a smallest unit\n of work that can be schedule to run",
			"lineHeight": 1.25
		},
		{
			"id": "LKC2_Mxx6b_mEywNUxcsL",
			"type": "arrow",
			"x": -884.2545719900008,
			"y": 11.199078843212867,
			"width": 3.950173587155632,
			"height": 91.34674376077444,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 910333656,
			"version": 517,
			"versionNonce": 926903512,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-3.950173587155632,
					-91.34674376077444
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "tCTWZf4i",
				"focus": 0.0953677084440547,
				"gap": 11.84339945887541
			},
			"endBinding": {
				"elementId": "oHFTOSre",
				"focus": -0.03664638485609088,
				"gap": 10.882086924094125
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "vr7JjT6yMWwcYJ28bAUIw",
			"type": "arrow",
			"x": -498.3042929861007,
			"y": 184.4707531818912,
			"width": 245.5762150293731,
			"height": 515.1860703357638,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 840281816,
			"version": 769,
			"versionNonce": 1841312168,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-245.5762150293731,
					515.1860703357638
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jhxSeelf",
				"focus": -0.3370566518998379,
				"gap": 3.967932345231816
			},
			"endBinding": {
				"elementId": "kpTN0hggM2La_1ySGld38",
				"focus": 0.3167944689193427,
				"gap": 7.784070628041718
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "kpTN0hggM2La_1ySGld38",
			"type": "rectangle",
			"x": -2045.232466923444,
			"y": 707.4408941456969,
			"width": 1605.4350646681157,
			"height": 766.7169050187892,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 2058862040,
			"version": 626,
			"versionNonce": 702348200,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "vr7JjT6yMWwcYJ28bAUIw",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "iZ9aX-EFO9za0yrs45Mop",
			"type": "rectangle",
			"x": -1226.442932840694,
			"y": 852.4557481939544,
			"width": 288.2267221674897,
			"height": 345.4961853913144,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 773573592,
			"version": 1319,
			"versionNonce": 756792488,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "wUHibU64Xuv1MwvGsv_1U",
			"type": "rectangle",
			"x": -1708.8258325425682,
			"y": 909.5171945632384,
			"width": 281.3251418973291,
			"height": 324.7916753000305,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1369278680,
			"version": 823,
			"versionNonce": 785246120,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "jjoE9ApikA7p2Ug3syqHk",
					"type": "arrow"
				},
				{
					"id": "7SrOpsBTMXdHYMJ-5vMVQ",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "x7daTO3z",
			"type": "text",
			"x": -1605.8248111029118,
			"y": 927.6281626925369,
			"width": 68.31991577148438,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1854176168,
			"version": 799,
			"versionNonce": 1344546984,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "7SrOpsBTMXdHYMJ-5vMVQ",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Pipeline",
			"rawText": "Pipeline",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Pipeline",
			"lineHeight": 1.25
		},
		{
			"id": "LXZ10Py01hsOgMpcY8gmg",
			"type": "rectangle",
			"x": -1685.818065859484,
			"y": 989.7273353760784,
			"width": 245.21722579759444,
			"height": 70.48162664016934,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1957255384,
			"version": 682,
			"versionNonce": 770233256,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "twqhnzLL"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "twqhnzLL",
			"type": "text",
			"x": -1592.0894273259212,
			"y": 1012.4681486961631,
			"width": 57.75994873046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1469411288,
			"version": 597,
			"versionNonce": 1675632296,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Stage",
			"rawText": "Stage",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "LXZ10Py01hsOgMpcY8gmg",
			"originalText": "Stage",
			"lineHeight": 1.25
		},
		{
			"id": "7xawT779w-jQpDAp0KNHm",
			"type": "rectangle",
			"x": -1685.0264852341018,
			"y": 1076.4805446808637,
			"width": 245.21722579759444,
			"height": 70.48162664016934,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 2062540200,
			"version": 733,
			"versionNonce": 313919912,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "eGAx8HOH"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "eGAx8HOH",
			"type": "text",
			"x": -1591.297846700539,
			"y": 1099.2213580009484,
			"width": 57.75994873046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1388589272,
			"version": 647,
			"versionNonce": 1704367272,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Stage",
			"rawText": "Stage",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "7xawT779w-jQpDAp0KNHm",
			"originalText": "Stage",
			"lineHeight": 1.25
		},
		{
			"id": "ImxHJkgPP56MoV1y8q61I",
			"type": "ellipse",
			"x": -1995.3577937764749,
			"y": 749.9036006569221,
			"width": 227.78758639027342,
			"height": 121.31981390346641,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2078245544,
			"version": 588,
			"versionNonce": 1110294440,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "jjoE9ApikA7p2Ug3syqHk",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "FAkm0mfF",
			"type": "text",
			"x": -1945.2037259842637,
			"y": 784.8952862019403,
			"width": 123.55195617675781,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 387483608,
			"version": 995,
			"versionNonce": 1940911528,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "jjoE9ApikA7p2Ug3syqHk",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Trigger",
			"rawText": "Trigger",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "Trigger",
			"lineHeight": 1.25
		},
		{
			"id": "jjoE9ApikA7p2Ug3syqHk",
			"type": "arrow",
			"x": -1776.6398180065262,
			"y": 839.1800945728922,
			"width": 89.63513643285137,
			"height": 69.05461325251554,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 428910040,
			"version": 2422,
			"versionNonce": 848894936,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					89.63513643285137,
					69.05461325251554
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "ImxHJkgPP56MoV1y8q61I",
				"focus": -0.48879277679857963,
				"gap": 3.1799472981807497
			},
			"endBinding": {
				"elementId": "wUHibU64Xuv1MwvGsv_1U",
				"focus": 0.26637170342498784,
				"gap": 1.2824867378306521
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "hAPpsNYVKkqj2uNuySMvW",
			"type": "rectangle",
			"x": -1353.630305273853,
			"y": 917.5952459174636,
			"width": 377.8017635151107,
			"height": 488.09964673404033,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1069685672,
			"version": 1050,
			"versionNonce": 110930856,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "7SrOpsBTMXdHYMJ-5vMVQ",
					"type": "arrow"
				},
				{
					"id": "1IgP32lqQuULKqVUK_rjw",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "oY-QWdrRiihaGrxFvp66R",
			"type": "rectangle",
			"x": -909.0998286033298,
			"y": 910.413813204921,
			"width": 377.8017635151107,
			"height": 348.1152172778864,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#eaddd7",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 2017739736,
			"version": 827,
			"versionNonce": 1404660904,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1IgP32lqQuULKqVUK_rjw",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "7SrOpsBTMXdHYMJ-5vMVQ",
			"type": "arrow",
			"x": -1569.545834167336,
			"y": 903.9161923207309,
			"width": 431.63629460455445,
			"height": 88.42946485692426,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1071812264,
			"version": 2296,
			"versionNonce": 1924531672,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					331.6019526835662,
					-84.16907385638217
				],
				[
					431.63629460455445,
					4.260391000542086
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "wUHibU64Xuv1MwvGsv_1U",
				"focus": -0.849813778809987,
				"gap": 5.601002242507491
			},
			"endBinding": {
				"elementId": "hAPpsNYVKkqj2uNuySMvW",
				"focus": 0.6743367394672055,
				"gap": 9.418662596190586
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "1IgP32lqQuULKqVUK_rjw",
			"type": "arrow",
			"x": -1000.2057020391123,
			"y": 1417.1197229793447,
			"width": 218.42082575212567,
			"height": 148.15800385413377,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 141421992,
			"version": 1971,
			"versionNonce": 203452376,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					132.81177554326132,
					3.1891650389000006
				],
				[
					218.42082575212567,
					-144.96883881523377
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "hAPpsNYVKkqj2uNuySMvW",
				"focus": 1.0118195098596698,
				"gap": 11.42483032784088
			},
			"endBinding": {
				"elementId": "oY-QWdrRiihaGrxFvp66R",
				"focus": -0.16187741381150145,
				"gap": 13.621853681303548
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "VcjJaQj5",
			"type": "text",
			"x": -1077.0081294171614,
			"y": 868.9857756308617,
			"width": 110.91990661621094,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 797534936,
			"version": 520,
			"versionNonce": 577362088,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Environment",
			"rawText": "Environment",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Environment",
			"lineHeight": 1.25
		},
		{
			"id": "T_02kxqh9MH99Dl_oHnbP",
			"type": "rectangle",
			"x": -1333.7921910707064,
			"y": 978.6958992235332,
			"width": 334.0960568260987,
			"height": 175.44713660992602,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 2099663064,
			"version": 610,
			"versionNonce": 200836008,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "Y2p0M9I47GiUVukLPnjYl",
			"type": "rectangle",
			"x": -1333.1245612433847,
			"y": 1194.0062959250904,
			"width": 334.0960568260987,
			"height": 175.44713660992602,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 309665240,
			"version": 662,
			"versionNonce": 1148833448,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "1IgP32lqQuULKqVUK_rjw",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "OfTXLyqd",
			"type": "text",
			"x": -1195.6742855661555,
			"y": 989.8946685551459,
			"width": 54.71995544433594,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1790769832,
			"version": 497,
			"versionNonce": 345618856,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Agent",
			"rawText": "Agent",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Agent",
			"lineHeight": 1.25
		},
		{
			"id": "6CdT3ypi",
			"type": "text",
			"x": -1187.54068472509,
			"y": 1201.4722669388352,
			"width": 54.71995544433594,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 54176680,
			"version": 560,
			"versionNonce": 1334068392,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Agent",
			"rawText": "Agent",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Agent",
			"lineHeight": 1.25
		},
		{
			"id": "mutEvnChd_3Xq5IQkk4ON",
			"type": "rectangle",
			"x": -1316.9939746769528,
			"y": 1040.289068151068,
			"width": 298.63334967232663,
			"height": 89.59002986023188,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 88737960,
			"version": 557,
			"versionNonce": 48590760,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "EacOcC8O"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "EacOcC8O",
			"type": "text",
			"x": -1184.6372836664732,
			"y": 1072.584083081184,
			"width": 33.91996765136719,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 900772008,
			"version": 444,
			"versionNonce": 652819112,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Job",
			"rawText": "Job",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "mutEvnChd_3Xq5IQkk4ON",
			"originalText": "Job",
			"lineHeight": 1.25
		},
		{
			"id": "kZ5689BT-EJkF1kkiAYoV",
			"type": "rectangle",
			"x": -1310.7268977874905,
			"y": 1251.8666665347573,
			"width": 298.63334967232663,
			"height": 89.59002986023188,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1674920664,
			"version": 635,
			"versionNonce": 1312531880,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "dojzPjCX"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "dojzPjCX",
			"type": "text",
			"x": -1178.370206777011,
			"y": 1284.1616814648733,
			"width": 33.91996765136719,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1630992040,
			"version": 521,
			"versionNonce": 1443410088,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Job",
			"rawText": "Job",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "kZ5689BT-EJkF1kkiAYoV",
			"originalText": "Job",
			"lineHeight": 1.25
		},
		{
			"id": "N1lkc7b7",
			"type": "text",
			"x": -1201.2736078356272,
			"y": 933.901071482421,
			"width": 57.75994873046875,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffc9c9",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 2037123240,
			"version": 387,
			"versionNonce": 368860072,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Stage",
			"rawText": "Stage",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Stage",
			"lineHeight": 1.25
		},
		{
			"id": "Jz823fMH",
			"type": "text",
			"x": -758.9229055966093,
			"y": 926.4352252613455,
			"width": 55.11993408203125,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1593081048,
			"version": 394,
			"versionNonce": 272803496,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Steps",
			"rawText": "Steps",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Steps",
			"lineHeight": 1.25
		},
		{
			"id": "S9h4CEGXWx7ojA716Qtwq",
			"type": "rectangle",
			"x": -887.7086905138196,
			"y": 991.761192506749,
			"width": 339.6953790955706,
			"height": 108.25464541291944,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1996082856,
			"version": 450,
			"versionNonce": 562532776,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "HetWugJ6"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "HetWugJ6",
			"type": "text",
			"x": -775.5809411515811,
			"y": 1033.3885152132088,
			"width": 115.43988037109375,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 151751848,
			"version": 372,
			"versionNonce": 821501096,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Step: Script",
			"rawText": "Step: Script",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "S9h4CEGXWx7ojA716Qtwq",
			"originalText": "Step: Script",
			"lineHeight": 1.25
		},
		{
			"id": "yJy9z-OCuU6m4JHymMEt1",
			"type": "rectangle",
			"x": -887.0411854791673,
			"y": 1125.199001003952,
			"width": 339.6953790955706,
			"height": 108.25464541291944,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1246187176,
			"version": 512,
			"versionNonce": 1614628776,
			"isDeleted": false,
			"boundElements": [
				{
					"type": "text",
					"id": "U2iYMFQs"
				},
				{
					"id": "1IgP32lqQuULKqVUK_rjw",
					"type": "arrow"
				},
				{
					"id": "fiEXDCubO-jAct4FJ9hWQ",
					"type": "arrow"
				},
				{
					"id": "_ksB-pRMvtEJ1cjsuaf7_",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false
		},
		{
			"id": "U2iYMFQs",
			"type": "text",
			"x": -771.7534477136087,
			"y": 1166.8263237104115,
			"width": 109.11990356445312,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#b2f2bb",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1536708568,
			"version": 439,
			"versionNonce": 1531938984,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Step: Task",
			"rawText": "Step: Task",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 17,
			"containerId": "yJy9z-OCuU6m4JHymMEt1",
			"originalText": "Step: Task",
			"lineHeight": 1.25
		},
		{
			"id": "3lSQUBbC",
			"type": "text",
			"x": -1352.462671555127,
			"y": 732.4684313139225,
			"width": 387.1438293457031,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1381195480,
			"version": 442,
			"versionNonce": 2091398056,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Key concepts overview",
			"rawText": "Key concepts overview",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "Key concepts overview",
			"lineHeight": 1.25
		},
		{
			"id": "fiEXDCubO-jAct4FJ9hWQ",
			"type": "arrow",
			"x": -682.6542449801043,
			"y": 1234.4536464168714,
			"width": 97.06652225845221,
			"height": 292.1980367042238,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 62617256,
			"version": 2208,
			"versionNonce": 695753176,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-97.06652225845221,
					292.1980367042238
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "yJy9z-OCuU6m4JHymMEt1",
				"focus": -0.28138562371411907,
				"gap": 1.0000000000001137
			},
			"endBinding": {
				"elementId": "JuCjPrBF",
				"focus": 0.33668216221654806,
				"gap": 15.007643021259355
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "JuCjPrBF",
			"type": "text",
			"x": -1112.1482836640635,
			"y": 1541.6593261423545,
			"width": 474.98382568359375,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1848805336,
			"version": 996,
			"versionNonce": 18704808,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "fiEXDCubO-jAct4FJ9hWQ",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "It is a prepackaged script",
			"rawText": "It is a prepackaged script",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "It is a prepackaged script",
			"lineHeight": 1.25
		},
		{
			"id": "k66aFm2Q",
			"type": "text",
			"x": -811.2386590471704,
			"y": 1630.1331980240188,
			"width": 377.02783203125,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 1725524648,
			"version": 653,
			"versionNonce": 104669096,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "_ksB-pRMvtEJ1cjsuaf7_",
					"type": "arrow"
				},
				{
					"id": "-RpJWogo99oL1kue8Mh3f",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "Publish build Artifact",
			"rawText": "Publish build Artifact",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "Publish build Artifact",
			"lineHeight": 1.25
		},
		{
			"id": "_ksB-pRMvtEJ1cjsuaf7_",
			"type": "arrow",
			"x": -636.3877227356284,
			"y": 1234.8701226158505,
			"width": 45.45735887440105,
			"height": 381.64306010169526,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 320556456,
			"version": 1476,
			"versionNonce": 1297990616,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					45.45735887440105,
					381.64306010169526
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "yJy9z-OCuU6m4JHymMEt1",
				"focus": -0.4208291078162273,
				"gap": 1.4164761989792396
			},
			"endBinding": {
				"elementId": "k66aFm2Q",
				"focus": 0.1887958961850289,
				"gap": 13.620015306473078
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "5FmeHYLR",
			"type": "text",
			"x": -1716.4669449990438,
			"y": 830.5064397587972,
			"width": 52.739990234375,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 428228776,
			"version": 305,
			"versionNonce": 402394024,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "run",
			"rawText": "run",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "run",
			"lineHeight": 1.25
		},
		{
			"id": "n6elMGvQ",
			"type": "text",
			"x": -2036.2360625085225,
			"y": 1520.6558532581357,
			"width": 694.8717041015625,
			"height": 90,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": null,
			"seed": 357043368,
			"version": 487,
			"versionNonce": 382490280,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "-RpJWogo99oL1kue8Mh3f",
					"type": "arrow"
				}
			],
			"updated": 1724273614329,
			"link": null,
			"locked": false,
			"text": "A Artifact is a collection\nof files or packages published by a run",
			"rawText": "A Artifact is a collection\nof files or packages published by a run",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 76,
			"containerId": null,
			"originalText": "A Artifact is a collection\nof files or packages published by a run",
			"lineHeight": 1.25
		},
		{
			"id": "-RpJWogo99oL1kue8Mh3f",
			"type": "arrow",
			"x": -821.5733162401166,
			"y": 1654.1583667899772,
			"width": 846.5831821189975,
			"height": 85.67068814631943,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [
				"UB8ibiKxv1DZw3jhywZT_"
			],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 853238184,
			"version": 1174,
			"versionNonce": 1383116248,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273614337,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-646.4399691019162,
					50.536960917265105
				],
				[
					-846.5831821189975,
					-35.13372722905433
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "k66aFm2Q",
				"focus": 0.37650965451002216,
				"gap": 10.334657192946224
			},
			"endBinding": {
				"elementId": "n6elMGvQ",
				"focus": 0.22988113249616196,
				"gap": 8.368786302787157
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "zDKc2f0u",
			"type": "text",
			"x": -320.4477989067723,
			"y": 717.4460401341839,
			"width": 47.48799133300781,
			"height": 35,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 370656984,
			"version": 120,
			"versionNonce": 1835742120,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "xsMEQO44DSwf7E4JiXhVn",
					"type": "arrow"
				},
				{
					"id": "VlfWQXRtrDMFKVt0EZiCF",
					"type": "arrow"
				},
				{
					"id": "fHe2OyYAodIaossGHoQ-C",
					"type": "arrow"
				},
				{
					"id": "Y-VXKcW4kflM_sjcmInan",
					"type": "arrow"
				}
			],
			"updated": 1724273059648,
			"link": null,
			"locked": false,
			"text": "Job",
			"rawText": "Job",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": "Job",
			"lineHeight": 1.25
		},
		{
			"id": "xsMEQO44DSwf7E4JiXhVn",
			"type": "arrow",
			"x": -453.7067660138699,
			"y": 185.0665457755191,
			"width": 164.18462641044385,
			"height": 520.4779909949035,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1099041192,
			"version": 590,
			"versionNonce": 141983656,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273077771,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					164.18462641044385,
					520.4779909949035
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jhxSeelf",
				"focus": -0.7999052711069103,
				"gap": 4.563724938859707
			},
			"endBinding": {
				"elementId": "zDKc2f0u",
				"focus": 0.5623343896012509,
				"gap": 11.901503363761321
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "G1PAGSuq",
			"type": "text",
			"x": -29.286740820131513,
			"y": 1298.9549924940334,
			"width": 282.55975341796875,
			"height": 275,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1854775512,
			"version": 348,
			"versionNonce": 204596904,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "-j8MHzuTweDQtkLtPKeyf",
					"type": "arrow"
				}
			],
			"updated": 1724273220265,
			"link": null,
			"locked": false,
			"text": "trigger:\n- main\n\npool:\n    vmImage: 'ubuntu-latest'\n\nsteps:\n- task: TaskName@1\n  inputs:\n    option : 'value'\n",
			"rawText": "trigger:\n- main\n\npool:\n    vmImage: 'ubuntu-latest'\n\nsteps:\n- task: TaskName@1\n  inputs:\n    option : 'value'\n",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 267,
			"containerId": null,
			"originalText": "trigger:\n- main\n\npool:\n    vmImage: 'ubuntu-latest'\n\nsteps:\n- task: TaskName@1\n  inputs:\n    option : 'value'\n",
			"lineHeight": 1.25
		},
		{
			"id": "Rv5wZLKc",
			"type": "text",
			"x": 296.39134241139675,
			"y": 791.9328232669451,
			"width": 215.93978881835938,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 73167016,
			"version": 271,
			"versionNonce": 1802399192,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "VlfWQXRtrDMFKVt0EZiCF",
					"type": "arrow"
				}
			],
			"updated": 1724273236301,
			"link": null,
			"locked": false,
			"text": "Deployment group jobs",
			"rawText": "Deployment group jobs",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Deployment group jobs",
			"lineHeight": 1.25
		},
		{
			"id": "0LbBQSy8",
			"type": "text",
			"x": 306.0743683059502,
			"y": 869.7615775313806,
			"width": 92.51992797851562,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 667684568,
			"version": 179,
			"versionNonce": 256363224,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "fHe2OyYAodIaossGHoQ-C",
					"type": "arrow"
				}
			],
			"updated": 1724273237454,
			"link": null,
			"locked": false,
			"text": "Agent job",
			"rawText": "Agent job",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 17,
			"containerId": null,
			"originalText": "Agent job",
			"lineHeight": 1.25
		},
		{
			"id": "VlfWQXRtrDMFKVt0EZiCF",
			"type": "arrow",
			"x": -266.2736440462737,
			"y": 731.2975803417733,
			"width": 558.7882410735729,
			"height": 50.324434815054246,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 56170920,
			"version": 314,
			"versionNonce": 803133400,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273236302,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					558.7882410735729,
					50.324434815054246
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "zDKc2f0u",
				"focus": -0.32558374676594015,
				"gap": 6.6861635274907485
			},
			"endBinding": {
				"elementId": "Rv5wZLKc",
				"focus": 0.573166078774114,
				"gap": 11.015530793238668
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "fHe2OyYAodIaossGHoQ-C",
			"type": "arrow",
			"x": -262.3271298745561,
			"y": 750.1029875106409,
			"width": 557.3861310543448,
			"height": 131.11774763643064,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1905477080,
			"version": 437,
			"versionNonce": 683996376,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273237454,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					557.3861310543448,
					131.11774763643064
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "zDKc2f0u",
				"focus": 0.3116361291976446,
				"gap": 10.632677699208386
			},
			"endBinding": {
				"elementId": "0LbBQSy8",
				"focus": -0.5317081458467394,
				"gap": 11.015367126161436
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "Uh7DPV3E",
			"type": "text",
			"x": 27.637086714537645,
			"y": 1104.9537916544366,
			"width": 122.69595336914062,
			"height": 35,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1934813912,
			"version": 184,
			"versionNonce": 1019255000,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "Y-VXKcW4kflM_sjcmInan",
					"type": "arrow"
				},
				{
					"id": "-j8MHzuTweDQtkLtPKeyf",
					"type": "arrow"
				},
				{
					"id": "XSAxOA9aZw08Y1ByKt_96",
					"type": "arrow"
				},
				{
					"id": "PzyovNiInXWVCtEN7jFUH",
					"type": "arrow"
				}
			],
			"updated": 1724273607285,
			"link": null,
			"locked": false,
			"text": "Examples",
			"rawText": "Examples",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": "Examples",
			"lineHeight": 1.25
		},
		{
			"id": "Y-VXKcW4kflM_sjcmInan",
			"type": "arrow",
			"x": -291.5248962678303,
			"y": 758.2232145647054,
			"width": 374.8724758935309,
			"height": 334.96201448803413,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1323920296,
			"version": 372,
			"versionNonce": 1064829864,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273234621,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					374.8724758935309,
					334.96201448803413
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "zDKc2f0u",
				"focus": 0.48357416070554904,
				"gap": 5.777174430521427
			},
			"endBinding": {
				"elementId": "Uh7DPV3E",
				"focus": 0.33507191924845936,
				"gap": 11.768562601697113
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "-j8MHzuTweDQtkLtPKeyf",
			"type": "arrow",
			"x": 63.845950079112185,
			"y": 1154.0188831466037,
			"width": 66.76243655175647,
			"height": 132.0869550485079,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1052626856,
			"version": 517,
			"versionNonce": 238631336,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273234621,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-66.76243655175647,
					132.0869550485079
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Uh7DPV3E",
				"focus": 0.13044630742239005,
				"gap": 14.065091492166971
			},
			"endBinding": {
				"elementId": "G1PAGSuq",
				"focus": -0.9057031090634888,
				"gap": 12.849154298921803
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "0_ZID_o_-bVhmAeJiyrOM",
			"type": "arrow",
			"x": -339.17664182448743,
			"y": -33.598132558571024,
			"width": 112.10831896999662,
			"height": 166.72504693556687,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 839849176,
			"version": 77,
			"versionNonce": 1481802920,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273087431,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-112.10831896999662,
					166.72504693556687
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "IkM6GrN9",
				"focus": 0.18164508912729035,
				"gap": 18.858452619437507
			},
			"endBinding": {
				"elementId": "jhxSeelf",
				"focus": 0.5661896799069683,
				"gap": 12.375906459663554
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "bLFOKM8i",
			"type": "text",
			"x": 345.9139153099122,
			"y": 1290.6604158041946,
			"width": 265.55987548828125,
			"height": 200,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 19364520,
			"version": 326,
			"versionNonce": 96055464,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "XSAxOA9aZw08Y1ByKt_96",
					"type": "arrow"
				}
			],
			"updated": 1724273230446,
			"link": null,
			"locked": false,
			"text": "strategy:\n    matrix:\n        linux:\n            imageName: \"...\"\n    ...\n    maxParallel: 3\n\npool: $(imageName)",
			"rawText": "strategy:\n    matrix:\n        linux:\n            imageName: \"...\"\n    ...\n    maxParallel: 3\n\npool: $(imageName)",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 192,
			"containerId": null,
			"originalText": "strategy:\n    matrix:\n        linux:\n            imageName: \"...\"\n    ...\n    maxParallel: 3\n\npool: $(imageName)",
			"lineHeight": 1.25
		},
		{
			"id": "XSAxOA9aZw08Y1ByKt_96",
			"type": "arrow",
			"x": 158.59882316832932,
			"y": 1147.5867465434258,
			"width": 186.73206875513847,
			"height": 115.69184377906959,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 2059455960,
			"version": 655,
			"versionNonce": 983887784,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273234621,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					186.73206875513847,
					115.69184377906959
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Uh7DPV3E",
				"focus": -0.3214798802460014,
				"gap": 11.251007525544082
			},
			"endBinding": {
				"elementId": "bLFOKM8i",
				"focus": 0.24555085061382123,
				"gap": 27.388031747085734
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "W4DXxTOZ",
			"type": "text",
			"x": 728.3176586448383,
			"y": 1284.9357514927003,
			"width": 358.29974365234375,
			"height": 275,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 679842008,
			"version": 400,
			"versionNonce": 1826767576,
			"isDeleted": false,
			"boundElements": [
				{
					"id": "PzyovNiInXWVCtEN7jFUH",
					"type": "arrow"
				}
			],
			"updated": 1724273607285,
			"link": null,
			"locked": false,
			"text": "jobs:\n- job: Name\n  dependsOn: JobName\n  condition: failed()\n  steps:\n  - script: echo Hello\n  - bash: |\n        echo Hello\n    env:\n      NAME: $(System.TeamProject)\n    displayName: 'Name'",
			"rawText": "jobs:\n- job: Name\n  dependsOn: JobName\n  condition: failed()\n  steps:\n  - script: echo Hello\n  - bash: |\n        echo Hello\n    env:\n      NAME: $(System.TeamProject)\n    displayName: 'Name'",
			"fontSize": 20,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 267,
			"containerId": null,
			"originalText": "jobs:\n- job: Name\n  dependsOn: JobName\n  condition: failed()\n  steps:\n  - script: echo Hello\n  - bash: |\n        echo Hello\n    env:\n      NAME: $(System.TeamProject)\n    displayName: 'Name'",
			"lineHeight": 1.25
		},
		{
			"id": "PzyovNiInXWVCtEN7jFUH",
			"type": "arrow",
			"x": 163.5162287707019,
			"y": 1131.0796123811435,
			"width": 573.9092641395571,
			"height": 132.44064124236934,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1093870760,
			"version": 116,
			"versionNonce": 926747560,
			"isDeleted": false,
			"boundElements": null,
			"updated": 1724273609099,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					573.9092641395571,
					132.44064124236934
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "Uh7DPV3E",
				"focus": -0.2708286367486437,
				"gap": 13.18318868702363
			},
			"endBinding": {
				"elementId": "W4DXxTOZ",
				"focus": 0.6691650754843324,
				"gap": 21.415497869187448
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "hSxdzQy6",
			"type": "text",
			"x": -1511.7602870530457,
			"y": 700.1200628536982,
			"width": 18,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 226636456,
			"version": 6,
			"versionNonce": 2130637016,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 31,
			"containerId": "wUHibU64Xuv1MwvGsv_1U",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "Fexblz-Gzh8644BF-Eq4S",
			"type": "arrow",
			"x": -326.40124294983633,
			"y": 15.211703678098338,
			"width": 26.90574538248319,
			"height": 108.49766745590483,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 24513448,
			"version": 351,
			"versionNonce": 985205160,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-26.90574538248319,
					108.49766745590483
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "IkM6GrN9",
				"focus": 0.8338467171561491,
				"gap": 10.176841998444168
			},
			"endBinding": {
				"elementId": "jhxSeelf",
				"focus": 0.840189023659984,
				"gap": 8.857863348674869
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "JUPidfBf",
			"type": "text",
			"x": 448.0412793289843,
			"y": 131.85140642726225,
			"width": 14,
			"height": 35,
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
			"seed": 855233240,
			"version": 11,
			"versionNonce": 812893400,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 25,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "f3WS3W2P5ETFTMlce1hyI",
			"type": "freedraw",
			"x": -261.6002013937571,
			"y": 506.26962819232074,
			"width": 172.377787600447,
			"height": 6.759923578468602,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffec99",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 60,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 448578728,
			"version": 62,
			"versionNonce": 1535806120,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					0,
					-2.253307859489553
				],
				[
					1.1266915941023967,
					-3.379961789234301
				],
				[
					3.3799994535919495,
					-3.379961789234301
				],
				[
					6.759923578468602,
					-3.379961789234301
				],
				[
					11.266539297447707,
					-3.379961789234301
				],
				[
					14.646538751039657,
					-3.379961789234301
				],
				[
					20.27977073540592,
					-3.379961789234301
				],
				[
					24.786386454385024,
					-3.379961789234301
				],
				[
					30.41961843875123,
					-3.379961789234301
				],
				[
					33.79961789234318,
					-3.379961789234301
				],
				[
					37.17954201721989,
					-4.506615718979106
				],
				[
					41.68615773619899,
					-4.506615718979106
				],
				[
					43.939465595688546,
					-4.506615718979106
				],
				[
					47.3193897205652,
					-4.506615718979106
				],
				[
					49.57269758005475,
					-4.506615718979106
				],
				[
					52.9526970336467,
					-4.506615718979106
				],
				[
					55.20600489313625,
					-4.506615718979106
				],
				[
					58.58592901801296,
					-4.506615718979106
				],
				[
					61.96592847160491,
					-4.506615718979106
				],
				[
					64.21923633109446,
					-4.506615718979106
				],
				[
					67.59916045597117,
					-4.506615718979106
				],
				[
					70.97908458084783,
					-4.506615718979106
				],
				[
					74.35908403443977,
					-3.379961789234301
				],
				[
					76.61239189392933,
					-1.1266539297448048
				],
				[
					77.73900815931648,
					0
				],
				[
					79.99231601880604,
					1.126653929744748
				],
				[
					83.37231547239799,
					1.126653929744748
				],
				[
					85.62562333188754,
					1.126653929744748
				],
				[
					87.87893119137709,
					2.253307859489496
				],
				[
					91.25885531625374,
					1.126653929744748
				],
				[
					93.5121631757433,
					1.126653929744748
				],
				[
					96.89208730062,
					1.126653929744748
				],
				[
					100.27208675421195,
					1.126653929744748
				],
				[
					102.52539461370151,
					0
				],
				[
					105.90531873857822,
					0
				],
				[
					110.41193445755732,
					0
				],
				[
					114.91855017653637,
					0
				],
				[
					119.42516589551548,
					0
				],
				[
					123.93178161449458,
					0
				],
				[
					127.31170573937129,
					0
				],
				[
					132.9450130524528,
					1.126653929744748
				],
				[
					137.4515534427166,
					1.126653929744748
				],
				[
					143.08486075579816,
					1.126653929744748
				],
				[
					148.7180927401643,
					1.126653929744748
				],
				[
					154.35140005324587,
					1.126653929744748
				],
				[
					161.1112483029993,
					1.126653929744748
				],
				[
					166.74455561608073,
					0
				],
				[
					170.12447974095738,
					0
				],
				[
					172.377787600447,
					1.126653929744748
				],
				[
					172.377787600447,
					2.253307859489496
				],
				[
					172.377787600447,
					2.253307859489496
				]
			],
			"pressures": [
				0.34765625,
				0.4013671875,
				0.447265625,
				0.45703125,
				0.4912109375,
				0.521484375,
				0.53125,
				0.5478515625,
				0.5537109375,
				0.5576171875,
				0.5673828125,
				0.59375,
				0.603515625,
				0.6123046875,
				0.6220703125,
				0.623046875,
				0.6259765625,
				0.62890625,
				0.6279296875,
				0.626953125,
				0.626953125,
				0.626953125,
				0.6279296875,
				0.625,
				0.623046875,
				0.623046875,
				0.623046875,
				0.6240234375,
				0.623046875,
				0.625,
				0.625,
				0.6240234375,
				0.626953125,
				0.625,
				0.6259765625,
				0.6259765625,
				0.625,
				0.6259765625,
				0.62109375,
				0.62109375,
				0.619140625,
				0.62109375,
				0.6201171875,
				0.619140625,
				0.619140625,
				0.619140625,
				0.6201171875,
				0.625,
				0.623046875,
				0.6015625,
				0.5029296875,
				0
			],
			"simulatePressure": false,
			"lastCommittedPoint": [
				172.377787600447,
				2.253307859489496
			]
		},
		{
			"id": "bqsTcQNAn0I3D8xikruPM",
			"type": "freedraw",
			"x": -259.3468935342676,
			"y": 507.3962821220655,
			"width": 181.39101903840515,
			"height": 6.759923578468658,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 2,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 60,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 716241320,
			"version": 104,
			"versionNonce": 1614205912,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					-1.1266162653870992,
					0
				],
				[
					-1.1266162653870992,
					-1.126653929744748
				],
				[
					0,
					-2.253307859489553
				],
				[
					1.1266915941024536,
					-2.253307859489553
				],
				[
					2.253307859489553,
					-2.253307859489553
				],
				[
					4.506615718979106,
					-2.253307859489553
				],
				[
					5.633307313081502,
					-2.253307859489553
				],
				[
					6.759923578468658,
					-2.253307859489553
				],
				[
					9.013231437958211,
					-2.253307859489553
				],
				[
					11.266539297447764,
					-1.126653929744748
				],
				[
					12.39323089155016,
					0
				],
				[
					14.646538751039714,
					0
				],
				[
					16.899771281814026,
					0
				],
				[
					19.15307914130358,
					0
				],
				[
					20.279770735405975,
					0
				],
				[
					21.406387000793075,
					0
				],
				[
					23.659694860282627,
					0
				],
				[
					24.786386454385024,
					0
				],
				[
					27.039694313874577,
					0
				],
				[
					28.166310579261733,
					0
				],
				[
					29.29300217336413,
					0
				],
				[
					30.419618438751286,
					-1.126653929744748
				],
				[
					31.546310032853683,
					-1.126653929744748
				],
				[
					32.67292629824084,
					-1.126653929744748
				],
				[
					34.92623415773039,
					0
				],
				[
					36.05292575183279,
					0
				],
				[
					37.179542017219944,
					0
				],
				[
					39.4328498767095,
					0
				],
				[
					41.68615773619905,
					0
				],
				[
					43.9394655956886,
					1.126653929744748
				],
				[
					46.1927734551781,
					2.2533078594896097
				],
				[
					48.44608131466765,
					2.2533078594896097
				],
				[
					51.82600543954436,
					1.126653929744748
				],
				[
					54.07931329903391,
					1.126653929744748
				],
				[
					55.20600489313631,
					1.126653929744748
				],
				[
					57.45931275262586,
					1.126653929744748
				],
				[
					59.712620612115415,
					2.2533078594896097
				],
				[
					61.96592847160497,
					1.126653929744748
				],
				[
					64.21916100237922,
					0
				],
				[
					65.34585259648168,
					0
				],
				[
					67.59916045597117,
					0
				],
				[
					69.85246831546073,
					0
				],
				[
					72.10577617495028,
					-1.126653929744748
				],
				[
					73.23239244033743,
					-1.126653929744748
				],
				[
					74.35908403443983,
					-1.126653929744748
				],
				[
					77.73900815931654,
					0
				],
				[
					78.86569975341894,
					0
				],
				[
					81.11900761290849,
					-1.126653929744748
				],
				[
					83.37231547239804,
					-1.126653929744748
				],
				[
					85.6256233318876,
					0
				],
				[
					87.87885586266185,
					1.126653929744748
				],
				[
					91.2588553162538,
					1.126653929744748
				],
				[
					94.63877944113051,
					0
				],
				[
					96.89208730062006,
					0
				],
				[
					99.14539516010962,
					-1.126653929744748
				],
				[
					102.52539461370156,
					-1.126653929744748
				],
				[
					104.77870247319112,
					-1.126653929744748
				],
				[
					108.15862659806783,
					-1.126653929744748
				],
				[
					111.53855072294448,
					-2.253307859489553
				],
				[
					113.79185858243403,
					-2.253307859489553
				],
				[
					116.04516644192358,
					-2.253307859489553
				],
				[
					118.29847430141314,
					-3.379961789234301
				],
				[
					120.55178216090269,
					-2.253307859489553
				],
				[
					122.80509002039224,
					-2.253307859489553
				],
				[
					125.0583978798818,
					-2.253307859489553
				],
				[
					126.18508947398419,
					-2.253307859489553
				],
				[
					129.5650135988609,
					-2.253307859489553
				],
				[
					131.8183214583504,
					-2.253307859489553
				],
				[
					134.07162931783995,
					-2.253307859489553
				],
				[
					136.3249371773295,
					-1.126653929744748
				],
				[
					138.57824503681906,
					-1.126653929744748
				],
				[
					140.83155289630866,
					-1.126653929744748
				],
				[
					144.21147702118532,
					-1.126653929744748
				],
				[
					146.4647848806748,
					0
				],
				[
					149.84478433426676,
					-1.126653929744748
				],
				[
					152.09809219375637,
					0
				],
				[
					154.35140005324587,
					0
				],
				[
					157.73132417812263,
					0
				],
				[
					161.1112483029993,
					0
				],
				[
					163.36455616248878,
					1.126653929744748
				],
				[
					165.6178640219784,
					1.126653929744748
				],
				[
					167.8711718814679,
					1.126653929744748
				],
				[
					170.1244797409575,
					2.2533078594896097
				],
				[
					172.377787600447,
					2.2533078594896097
				],
				[
					174.6310954599366,
					2.2533078594896097
				],
				[
					175.75778705403894,
					1.126653929744748
				],
				[
					176.8844033194261,
					1.126653929744748
				],
				[
					178.01109491352855,
					2.2533078594896097
				],
				[
					179.1377111789157,
					2.2533078594896097
				],
				[
					179.1377111789157,
					1.126653929744748
				],
				[
					180.26440277301805,
					1.126653929744748
				],
				[
					179.1377111789157,
					1.126653929744748
				],
				[
					178.01109491352855,
					3.3799617892343576
				],
				[
					178.01109491352855,
					3.3799617892343576
				]
			],
			"pressures": [
				0.083984375,
				0.1953125,
				0.3408203125,
				0.4267578125,
				0.47265625,
				0.494140625,
				0.515625,
				0.5205078125,
				0.521484375,
				0.5263671875,
				0.5302734375,
				0.529296875,
				0.5302734375,
				0.5341796875,
				0.5341796875,
				0.53515625,
				0.541015625,
				0.541015625,
				0.5439453125,
				0.5458984375,
				0.546875,
				0.5478515625,
				0.5517578125,
				0.5537109375,
				0.5556640625,
				0.5595703125,
				0.560546875,
				0.560546875,
				0.5625,
				0.564453125,
				0.564453125,
				0.5625,
				0.564453125,
				0.5654296875,
				0.56640625,
				0.5654296875,
				0.5654296875,
				0.564453125,
				0.564453125,
				0.5654296875,
				0.5654296875,
				0.564453125,
				0.564453125,
				0.564453125,
				0.564453125,
				0.564453125,
				0.5634765625,
				0.5634765625,
				0.5654296875,
				0.564453125,
				0.5634765625,
				0.5625,
				0.5654296875,
				0.5654296875,
				0.5654296875,
				0.56640625,
				0.568359375,
				0.5673828125,
				0.5693359375,
				0.5712890625,
				0.5693359375,
				0.5673828125,
				0.5712890625,
				0.572265625,
				0.5732421875,
				0.576171875,
				0.578125,
				0.578125,
				0.578125,
				0.5791015625,
				0.5810546875,
				0.580078125,
				0.580078125,
				0.580078125,
				0.5810546875,
				0.5810546875,
				0.5810546875,
				0.5810546875,
				0.5810546875,
				0.5830078125,
				0.5869140625,
				0.5859375,
				0.5859375,
				0.5869140625,
				0.5859375,
				0.5869140625,
				0.5869140625,
				0.5888671875,
				0.5869140625,
				0.5869140625,
				0.587890625,
				0.5888671875,
				0.5908203125,
				0.15625,
				0
			],
			"simulatePressure": false,
			"lastCommittedPoint": [
				178.01109491352855,
				3.3799617892343576
			]
		},
		{
			"id": "d6vR5TYAJcsWO4qKpbFur",
			"type": "freedraw",
			"x": -262.7268176591461,
			"y": 479.7932985076761,
			"width": 248.99017949437638,
			"height": 5.6333073130814455,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 30,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1791201752,
			"version": 100,
			"versionNonce": 652122328,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					1.1266915941023967,
					-1.1266915941024536
				],
				[
					2.253307859489553,
					-2.2533078594896097
				],
				[
					4.506615718979106,
					-2.2533078594896097
				],
				[
					5.633307313081502,
					-3.3799994535919495
				],
				[
					6.759923578468658,
					-3.3799994535919495
				],
				[
					9.013231437958211,
					-2.2533078594896097
				],
				[
					11.266539297447764,
					-2.2533078594896097
				],
				[
					13.519847156937317,
					-2.2533078594896097
				],
				[
					16.899846610529266,
					-2.2533078594896097
				],
				[
					19.15307914130352,
					-2.2533078594896097
				],
				[
					21.406387000793075,
					-2.2533078594896097
				],
				[
					23.659694860282627,
					-2.2533078594896097
				],
				[
					27.039694313874577,
					-2.2533078594896097
				],
				[
					29.29300217336413,
					-3.3799994535919495
				],
				[
					32.67292629824084,
					-2.2533078594896097
				],
				[
					36.05292575183279,
					-2.2533078594896097
				],
				[
					39.4328498767095,
					-2.2533078594896097
				],
				[
					42.81277400158615,
					-2.2533078594896097
				],
				[
					46.1927734551781,
					-2.2533078594896097
				],
				[
					48.44608131466765,
					-2.2533078594896097
				],
				[
					51.82600543954436,
					-1.1266915941024536
				],
				[
					54.07931329903391,
					0
				],
				[
					56.332621158523466,
					1.126616265387156
				],
				[
					59.712620612115415,
					1.126616265387156
				],
				[
					61.96592847160497,
					1.126616265387156
				],
				[
					64.21923633109452,
					1.126616265387156
				],
				[
					66.47246886186878,
					2.253307859489496
				],
				[
					69.85246831546073,
					2.253307859489496
				],
				[
					72.10577617495034,
					1.126616265387156
				],
				[
					74.35908403443983,
					1.126616265387156
				],
				[
					77.73900815931648,
					0
				],
				[
					79.9923160188061,
					0
				],
				[
					83.37231547239804,
					0
				],
				[
					86.7522395972747,
					0
				],
				[
					89.0055474567643,
					0
				],
				[
					91.2588553162538,
					0
				],
				[
					94.63877944113045,
					-1.1266915941024536
				],
				[
					98.0187788947224,
					-1.1266915941024536
				],
				[
					101.39870301959917,
					-1.1266915941024536
				],
				[
					103.65201087908866,
					0
				],
				[
					105.90531873857827,
					0
				],
				[
					109.28531819217022,
					-1.1266915941024536
				],
				[
					111.53862605165972,
					-1.1266915941024536
				],
				[
					114.91855017653648,
					-1.1266915941024536
				],
				[
					118.29847430141314,
					-1.1266915941024536
				],
				[
					120.55178216090263,
					-1.1266915941024536
				],
				[
					123.93178161449458,
					-1.1266915941024536
				],
				[
					127.31170573937135,
					-1.1266915941024536
				],
				[
					130.6917051929633,
					-1.1266915941024536
				],
				[
					134.07162931783995,
					0
				],
				[
					137.4516287714319,
					0
				],
				[
					140.83155289630855,
					0
				],
				[
					143.08486075579816,
					0
				],
				[
					147.59147647477727,
					0
				],
				[
					149.84478433426676,
					0
				],
				[
					153.22470845914353,
					0
				],
				[
					157.73132417812263,
					0
				],
				[
					161.11132363171458,
					0
				],
				[
					164.49124775659124,
					1.126616265387156
				],
				[
					167.8711718814679,
					1.126616265387156
				],
				[
					172.377787600447,
					1.126616265387156
				],
				[
					175.75778705403894,
					1.126616265387156
				],
				[
					179.1377111789157,
					1.126616265387156
				],
				[
					183.6443268978947,
					1.126616265387156
				],
				[
					187.02425102277147,
					2.253307859489496
				],
				[
					191.53086674175057,
					2.253307859489496
				],
				[
					194.91086619534252,
					1.126616265387156
				],
				[
					198.29079032021917,
					1.126616265387156
				],
				[
					200.54409817970878,
					0
				],
				[
					203.92409763330073,
					0
				],
				[
					206.17740549279023,
					0
				],
				[
					209.55732961766688,
					0
				],
				[
					212.93725374254365,
					-1.1266915941024536
				],
				[
					216.3172531961356,
					-1.1266915941024536
				],
				[
					218.5705610556251,
					-1.1266915941024536
				],
				[
					221.95048518050186,
					-1.1266915941024536
				],
				[
					225.3304846340938,
					-1.1266915941024536
				],
				[
					228.71040875897046,
					-1.1266915941024536
				],
				[
					230.96371661845996,
					-1.1266915941024536
				],
				[
					233.21702447794956,
					-1.1266915941024536
				],
				[
					235.47033233743906,
					-1.1266915941024536
				],
				[
					237.72364019692867,
					0
				],
				[
					239.97694805641817,
					0
				],
				[
					242.23025591590778,
					1.126616265387156
				],
				[
					243.35687218129493,
					1.126616265387156
				],
				[
					244.48356377539727,
					1.126616265387156
				],
				[
					246.73687163488688,
					1.126616265387156
				],
				[
					247.86348790027392,
					0
				],
				[
					248.99017949437638,
					1.126616265387156
				],
				[
					247.86348790027392,
					2.253307859489496
				],
				[
					247.86348790027392,
					2.253307859489496
				]
			],
			"pressures": [
				0.0439453125,
				0.3056640625,
				0.3525390625,
				0.3837890625,
				0.41015625,
				0.416015625,
				0.4345703125,
				0.455078125,
				0.4638671875,
				0.470703125,
				0.482421875,
				0.4892578125,
				0.494140625,
				0.5,
				0.501953125,
				0.5029296875,
				0.5078125,
				0.5126953125,
				0.515625,
				0.517578125,
				0.51953125,
				0.5244140625,
				0.5263671875,
				0.529296875,
				0.533203125,
				0.5341796875,
				0.5361328125,
				0.5380859375,
				0.5400390625,
				0.5400390625,
				0.5400390625,
				0.541015625,
				0.541015625,
				0.541015625,
				0.5419921875,
				0.546875,
				0.5498046875,
				0.5537109375,
				0.5546875,
				0.5537109375,
				0.5556640625,
				0.5576171875,
				0.5595703125,
				0.5595703125,
				0.5615234375,
				0.560546875,
				0.560546875,
				0.5595703125,
				0.560546875,
				0.5595703125,
				0.5595703125,
				0.55859375,
				0.5595703125,
				0.5615234375,
				0.5595703125,
				0.560546875,
				0.5595703125,
				0.5595703125,
				0.55859375,
				0.5595703125,
				0.5576171875,
				0.5576171875,
				0.556640625,
				0.556640625,
				0.5556640625,
				0.5576171875,
				0.5595703125,
				0.5615234375,
				0.5654296875,
				0.5703125,
				0.572265625,
				0.5732421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.57421875,
				0.576171875,
				0.57421875,
				0.5732421875,
				0.57421875,
				0.576171875,
				0.5771484375,
				0.5791015625,
				0.5791015625,
				0.580078125,
				0.5068359375,
				0.109375,
				0
			],
			"simulatePressure": false,
			"lastCommittedPoint": [
				247.86348790027392,
				2.253307859489496
			]
		},
		{
			"id": "Uwh2n4Fw",
			"type": "text",
			"x": -853.6558810335181,
			"y": 225.73323282598471,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#f08c00",
			"backgroundColor": "transparent",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 30,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1123089064,
			"version": 10,
			"versionNonce": 776322520,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
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
		},
		{
			"id": "Q0V36G5s",
			"type": "text",
			"x": -648.6281970040777,
			"y": 64.66867085293622,
			"width": 14,
			"height": 35,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1606306264,
			"version": 2,
			"versionNonce": 423221672,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273081961,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 28,
			"fontFamily": 1,
			"textAlign": "center",
			"verticalAlign": "middle",
			"baseline": 25,
			"containerId": "6YkxYoOkslY5ya9c57Qyc",
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "5hGvqMdi",
			"type": "text",
			"x": -1346.7803522657987,
			"y": 341.9684119195981,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#a5d8ff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 202818728,
			"version": 3,
			"versionNonce": 1885105320,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
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
		},
		{
			"id": "AGt9w3yiLcFS-5Np8Vwvo",
			"type": "line",
			"x": -625.9450008827428,
			"y": 1017.3066960548686,
			"width": 415.08775489708773,
			"height": 93.18301451063076,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1436372184,
			"version": 190,
			"versionNonce": 645437352,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					415.08775489708773,
					93.18301451063076
				]
			],
			"lastCommittedPoint": null,
			"startBinding": null,
			"endBinding": null,
			"startArrowhead": null,
			"endArrowhead": null
		},
		{
			"id": "WfDYHezb",
			"type": "text",
			"x": -380.28059979284103,
			"y": 1106.2541125605965,
			"width": 18,
			"height": 45,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#d0bfff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 900654296,
			"version": 3,
			"versionNonce": 213653208,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059647,
			"link": null,
			"locked": false,
			"text": "",
			"rawText": "",
			"fontSize": 36,
			"fontFamily": 1,
			"textAlign": "left",
			"verticalAlign": "top",
			"baseline": 31,
			"containerId": null,
			"originalText": "",
			"lineHeight": 1.25
		},
		{
			"id": "OKZa9mkkaSrHHt6KZZdR8",
			"type": "arrow",
			"x": -466.08511250483957,
			"y": 143.18792598564806,
			"width": 123.5639426937613,
			"height": 179.66068133846915,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": {
				"type": 2
			},
			"seed": 1274108840,
			"version": 198,
			"versionNonce": 1521347240,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273059648,
			"link": null,
			"locked": false,
			"points": [
				[
					0,
					0
				],
				[
					123.5639426937613,
					-179.66068133846915
				]
			],
			"lastCommittedPoint": null,
			"startBinding": {
				"elementId": "jhxSeelf",
				"focus": 0.4403230858901957,
				"gap": 2.3148948510113314
			},
			"endBinding": {
				"elementId": "IkM6GrN9",
				"focus": 0.19840091724583878,
				"gap": 15.983829825187449
			},
			"startArrowhead": null,
			"endArrowhead": "arrow"
		},
		{
			"id": "nnUVhK6M",
			"type": "text",
			"x": 794.2584936734643,
			"y": 1295.5701020038573,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 1095195560,
			"version": 2,
			"versionNonce": 635664344,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273328303,
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
		},
		{
			"id": "lxwdNSaB",
			"type": "text",
			"x": 1451.353245139988,
			"y": 495.26239621709425,
			"width": 10,
			"height": 25,
			"angle": 0,
			"strokeColor": "#1e1e1e",
			"backgroundColor": "#ffffff",
			"fillStyle": "solid",
			"strokeWidth": 4,
			"strokeStyle": "solid",
			"roughness": 1,
			"opacity": 100,
			"groupIds": [],
			"frameId": null,
			"roundness": null,
			"seed": 2082610344,
			"version": 2,
			"versionNonce": 1799317208,
			"isDeleted": true,
			"boundElements": null,
			"updated": 1724273331389,
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
		"currentItemBackgroundColor": "#ffffff",
		"currentItemFillStyle": "solid",
		"currentItemStrokeWidth": 4,
		"currentItemStrokeStyle": "solid",
		"currentItemRoughness": 1,
		"currentItemOpacity": 100,
		"currentItemFontFamily": 1,
		"currentItemFontSize": 20,
		"currentItemTextAlign": "left",
		"currentItemStartArrowhead": null,
		"currentItemEndArrowhead": "arrow",
		"scrollX": 2851.771639120068,
		"scrollY": 582.6087113551146,
		"zoom": {
			"value": 0.29677016115094834
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