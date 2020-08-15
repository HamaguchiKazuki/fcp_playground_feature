# fcp_playground_feature
ICT内で必要だけど触ったことないものを触る場所　手触りを求めて
- ここは必要なものを作る予定だから基礎の理論や実装は[こっちでやる](https://github.com/HamaguchiKazuki/train_web_go)

## 動作環境(Ubuntu(Vagrant))
- kubernetes(kubeadm)
    - master 
    - node01
    - node02
- python
    - flask

## kubernetes
1. start env
```bash
vagrant up master node01 node02
```
2. copy join_token of node01 node02

## python
1. start enc
```bash
vagrant up python
```
2. docker-compose up
```bash
cd /vagrant && docker-compose -f deployments/docker-compose.yaml up -d
```
