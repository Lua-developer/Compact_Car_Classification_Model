# Compact_Car_Classification_Model

경차 이미지 학습 모델입니다.

2022년 5월 기준 현대 캐스퍼, 기아 모닝, 기아 레이 3개의 차종으로 구성되어 있으며 인식 가능 차량은 캐스퍼, 모닝, 스파크, 레이 등의 전면부 이미지를 분류 가능합니다.  

사용된 원천 데이터는 중고차 플랫폼 Encar에서 차량 전면부를 크롤링 하여 사용하였으며 컬러 214 흑백 160장 정도 학습 데이터로 사용되었습니다. 

라벨은 Compact, Other 두가지 라벨이 있으며 compact는 경차라벨을, Other은 경차가 아닌 이미지(테슬라, 투싼, etc...)등으로 학습 시켜 경차와 아닌 차로 분리를 하여 처리 할 수 있습니다.

## Example Image Hyundai Casper
![image](https://user-images.githubusercontent.com/83262616/168312753-afabcdad-39ea-417c-8ef2-f2a4bc49f455.png)
![KakaoTalk_20220513_235248760](https://user-images.githubusercontent.com/83262616/168313288-4070552d-bb6b-4a92-adea-a72ef1351a0d.png)
