# BooleanSim

BooleanSim은 Albert라는 사람이 개발한 이진네트워크 시뮬레이터인 [boolean2](https://github.com/ialbert/booleannet)를 python 3에서도 실행이 가능하도록 개선하고 몇개의 편리한 기능을 추가한 것입니다. python 3에서 실행되도록 하기 위해 [2to3.py](https://docs.python.org/3.0/library/2to3.html)와 [ply](http://www.dabeaz.com/ply)를 이용하였습니다.

BooleanSim은 boolean3와 boolean3_addon 모듈로 구성됩니다. boolean3는 Albert의 시뮬레이터와 동일하며 boolean3_addon에서는 boolean network의 basin크기를 추정하는 기능이 포함되어 있습니다.

### Installation

```
git clone git@github.com:jehoons/BooleanSim.git
cd BooleanSim 
python setup.py install 
```

### Test - Hello 

다음과 같이 간단한 모델에 대해서 시뮬레이션을 실행해 볼 수 있습니다. 

```python
import pickle 
from pdb import set_trace
from boolean3 import Model

def test_hello():
    text = """
    # initial values
    A = True
    B = Random
    C = Random
    # updating rules
    B* = A
    C* = B
    """
    model = Model( text=text, mode='sync')
    model.initialize()
    model.iterate( steps=10, repeat=1)
    
    for state in model.states:
        print (state.A, state.B, state.C)
```

### Test - Basin크기 추정하기 

boolean3_addon 모듈에서는 boolean network의 basin 크기를 추정할수 있는 `find_attractors` 함수를 지원합니다. 다음과 같이 실행해 봅시다:

```python 
import json
from ipdb import set_trace
from boolean3 import Model
from boolean3_addon import attractor

text = """
A = True
B = Random
C = Random
D = Random

B* = A or C
C* = A and not D
D* = B and C
"""

model = Model( text=text, mode='sync')
res = attractor.find_attractors(model=model, steps=10, sample_size=100)

outputfile = 'output.json'
json.dump(res, open(outputfile, 'w'), indent=1)
```

계산된 베이신에 관한 정보는 다음과 같이 계산이 될 것입니다:

```json
{
 "fingerprint_map_keys": [
  "A",
  "B",
  "C",
  "D"
 ],
 "cyclic_attractor_info": {
  "8db3eaf0539d9f77d663": "4123"
 },
 "fingerprint_map": {
  "2": [
   true,
   true,
   true,
   false
  ],
  "7": [
   true,
   false,
   false,
   false
  ],
  "0": [
   true,
   false,
   false,
   true
  ],
  "5": [
   true,
   false,
   true,
   false
  ],
  "6": [
   true,
   false,
   true,
   true
  ],
  "4": [
   true,
   true,
   false,
   true
  ],
  "3": [
   true,
   true,
   true,
   true
  ],
  "1": [
   true,
   true,
   false,
   false
  ]
 },
 "attractor_info": {
  "8db3eaf0539d9f77d663": "cyclic"
 },
 "attractors": {
  "2": {
   "type": "cyclic",
   "initial": 2,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 0,
   "trajectory": "2341234123"
  },
  "7": {
   "type": "cyclic",
   "initial": 7,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 1,
   "trajectory": "7234123412"
  },
  "0": {
   "type": "cyclic",
   "initial": 0,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 1,
   "trajectory": "0123412341"
  },
  "5": {
   "type": "cyclic",
   "initial": 5,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 1,
   "trajectory": "5234123412"
  },
  "6": {
   "type": "cyclic",
   "initial": 6,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 1,
   "trajectory": "6123412341"
  },
  "1": {
   "type": "cyclic",
   "initial": 1,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 0,
   "trajectory": "1234123412"
  },
  "3": {
   "type": "cyclic",
   "initial": 3,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 0,
   "trajectory": "3412341234"
  },
  "4": {
   "type": "cyclic",
   "initial": 4,
   "attractor": "4a5b0b3fd8eb9a324e8a",
   "size": 4,
   "index": 0,
   "trajectory": "4123412341"
  }
 },
 "basin_of_attraction": {
  "8db3eaf0539d9f77d663": 8
 }
}
```

### Test - Basin 크기 추정하기 (cython mode)

또한 빠르게 베이신 크기를 추정하는 모듈인 `attr_cy`를 제공합니다. 단, 이 코드는 충분히 검증되지는 않은 코드이므로 실행결과를 사용하기에 앞서서 올바른 결과인지 체크할 필요가 있습니다. normal mode에서와는 출력 JSON파일의 구조가 다르다는 것에 주의해야 합니다.

```python 
import json
from os.path import exists
from boolean3_addon import attr_cy

modeltext = '''
A= Random
B= Random
C= Random
A*= A or C
B*= A and C
C*= not A or B
'''

attr_cy.build(modeltext)

import pyximport; pyximport.install()

res = attr_cy.run(samples=10000, steps=50, 
    debug=False, on_states=['A'], progress=True)

json.dump(res, open('test_attr_cy.json', 'w'), indent=4)
```

위의 코드를 실행하면 다음과 같은 JSON 출력파일을 생성합니다. keyword argument, `debug=False`로 세팅하면 trajectory가 생략됩니다. trajectory를 보기 위해서는 `debug=True`로 설정해야 합니다.

```json 
{
    "parameters": {
        "samples": 1000000,
        "steps": 50
    },
    "attractors": {
        "7eaed65c90": {
            "ratio": 0.750524,
            "value": [
                "4ae1123067",
                "ce58123727"
            ],
            "count": 750524,
            "type": "cyclic"
        },
        "904154d19e": {
            "ratio": 0.12422,
            "value": "904154d19e",
            "count": 124220,
            "type": "point"
        },
        "86f1027545": {
            "ratio": 0.125256,
            "value": "86f1027545",
            "count": 125256,
            "type": "point"
        }
    },
    "state_key": {
        "904154d19e": "100",
        "ce58123727": "110",
        "4ae1123067": "101",
        "86f1027545": "111"
    },
    "labels": [
        "A",
        "B",
        "C"
    ],
    "trajectory": {}
}
```