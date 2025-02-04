#!bin/bash/python3
# wadl
from mywadl.survey import Survey
from mywadl.mission import Mission
# paramters
from mywadl.solver.solver import SolverParameters
from mywadl.lib.route import RouteParameters
from mywadl.mission import MissionParameters
for i in range(1):
    #read keypoints in txt file
    fr = open("PathplanningIn.txt",'r')
    linelist=[]
    for line in fr.readlines():
        line=line.replace("\n","")
        linevalue=float(line)
        linelist.append(linevalue)
    fr.close()
    A_long=linelist[0]
    A_lat=linelist[1]
    B_long=linelist[2]
    B_lat=linelist[3]
    C_long=linelist[4]
    C_lat=linelist[5]
    D_long=linelist[6]
    D_lat=linelist[7]
    
    # A_long=91.83756256103516
    # A_lat=35.47226497
    # B_long=91.82593536376953
    # B_lat=35.47226497
    # C_long=91.83485412597656
    # C_lat=35.47226497
    # D_long=91.85092163085938
    # D_lat=35.47226497
    E_long=linelist[9]
    E_lat=linelist[8]
    F_lat=linelist[11]
    F_long=linelist[10]
    G_lat=linelist[13]
    G_long=linelist[12]
    H_lat=linelist[15]
    H_long=linelist[14]
    I_lat=linelist[17]
    I_long=linelist[16]
    J_lat=linelist[18]
    J_long=linelist[19]
    # suvey design script
    # get file name
    # files are assumed geofences (ID, lat, long)
    file = "ZhuonaiLake.csv"
    
    # make survey
    name = 'Multi-drones'
    survey = Survey(name)
    
    # add the keypoints
    keyPoints = {"A": (A_lat, A_long),
                  "B":  (B_lat, B_long),
                "C":  (C_lat, C_long),
                  "D":  (D_lat, D_long),
                 "E":  (E_lat, E_long),
                 "F":  (F_lat, F_long),
                 "G":  (G_lat, G_long),
                 "H":  (H_lat, H_long),
                 "I":  (I_lat, I_long),
                 "J":  (J_lat, J_long)
                 }
    survey.setKeyPoints(keyPoints)
    
    # route paramters
    routeParams = RouteParameters() #todo
    routeParams["limit"] = 70  # s
    routeParams["speed"] = 2.5 # m/s
    routeParams["altitude"] = 2.  # m
    # add the tasks
    
    survey.addTask(file,
                   step=1.0,
                   home=["A","B","C","D","E","F","G","H","I","J"],
                   routeParameters=routeParams,
                   )#Step todo
    
    # solver parameters
    solverParams = SolverParameters()
    solverParams["subGraph_size"] = 40 #Todo
    solverParams["SATBound_offset"] = 2
    solverParams["timeout"] = 20
    
    # set the solver parameters
    survey.setSolverParamters(solverParams)
    
    # plan the survey
    view = 0
    # view current plan
    if view == 1:
        survey.view()
    else:
        # run path solver to plan paths and write output
        #print(1)
        survey.plan()
        #survey.plot()
    
    #make mission
    #mission paramters
    missionParams = MissionParameters()
    missionParams["N_bands"] = 1
    missionParams["autoland"] = True
    
    missionParams["assign"] = "sequence"
    
    missionParams["offset_takeoff_dist"] = 5
    missionParams["offset_land_dist"] = 10
    
    
    mission = Mission(missionParams)
    mission.fromSurvey(survey, showPlot=True)
    mission.setVersion(4, 0, 187)
    mission.write()
