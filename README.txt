pip install utm    
pip install shapely
pip install scipy==1.8.0
pip install z3-solver 

test: Run PathPlanning.py

#打包.py为.exe
cmd
cd C:\Users\13471\Desktop\OneStartingPoint
pyinstaller -F  PathPlanning.py

#PathplanningIn
oval_lat=linelist[0]
oval_long=linelist[1]
MSL_lat=linelist[2]
MSL_long=linelist[3]

#四个起点的约束条件及初始值
##测试1：四个起点在右侧直线
lat=[ 35.47080597:35.49739746]  初始值：35.484101715
lon=91.86079024

##测试2：四个起点在下侧直线
lat=35.47226497
lon=[ 91.81043460 : 91.86079024 ] 初始值：91.83561242

##测试3：有两个起点分别在下侧、右侧直线
lat=[ 35.47080597:35.49739746]  初始值：35.484101715
lon=91.86079024

lat=35.47226497
lon=[ 91.81043460 : 91.86079024 ] 初始值：91.83561242

