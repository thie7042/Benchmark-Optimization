# Save by TommyHielscher on 2022_04_12-13.19.16; build 2021 2020_03_07-01.50.37 167380
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
import time

t_file = open('C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/number_of_sols.txt','r')
num_it  = t_file.read()
num_it = num_it.split(' ')
iterations = int(num_it[0])
print("Number of simulations required: " + str(iterations))

algorithm = str(num_it[-1])

print("Optimization Algorithm: ", algorithm)


# Creating our optimization loop
sol = 1
sol = 1011
analysis = True
while analysis == True:

    
    # ====================== Check Termination Function ======================
    termination_file = 'C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/termination.txt'
    file_t = open(termination_file,'r')
    data_t = file_t.read()
    data_t = data_t.split(',')
    termination = data_t[0]
    if termination == "True":
        print("End of analysis")
        analysis = False
        continue
    # ====================== Set Directory ======================

    os.chdir(
        r"C:\Users\TommyHielscher\Desktop\Benchmark Optimization\10 Bar Truss")

    session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)
    
    # ====================== Define Parameters ====================== 

    param_file = 'C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/parameters.txt'
    
    
    if algorithm == "PSO":
        
        param_file = 'C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/parameters' + str(sol) + '.txt'
    if algorithm == "GA":
        
        param_file = 'C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Control/parameters' + str(sol) + '.txt'
    
    
    while True:
        time.sleep(2)
        try: 
            file_p = open(param_file,'r')
            data = file_p.read()
            data = data.split(',')
              
            area1 = float(data[0])
            area2 = float(data[1])
            area3 = float(data[2])
            area4 = float(data[3])
            area5 = float(data[4])
            area6 = float(data[5])
            area7 = float(data[6])
            area8 = float(data[7])
            area9 = float(data[8])
            area10 = float(data[9])
            phase = data[-1]
        except:
            print('File has not been created. Waiting for solver')
            
        if phase == "newdata":
            print("New data found!")
            break
        else:
            print("Waiting for new data")

    
    
    """area1 = 0.001
    area2 = 0.001
    area3 = 0.001
    area4 = 0.001    
    area5 = 0.001
    area6 = 0.001
    area7 = 0.001
    area8 = 0.001
    area9 = 0.001
    area10 = 0.001"""
    
    # ====================== Create Model ====================== 
    #mdb.Model(modelType=STANDARD_EXPLICIT, name='Truss')


    # ====================== Create 10 Bar Truss ====================== 
    """mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
        1.0, 0.0))

    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0, 0.0), point2=(
        2.0, 0.0))

    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(2.0, 0.0), point2=(
        2.0, 1.0))
    
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(2.0, 1.0), point2=(
        1.0, 1.0))
   
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0, 1.0), point2=(
        0.0, 1.0))
    
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0, 1.0), point2=(
        1.0, 0.0))
   
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 1.0), point2=(
        1.0, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
        1.0, 1.0))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0, 0.0), point2=(
        2.0, 1.0))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(1.0, 1.0), point2=(
        2.0, 0.0))
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseWire(sketch=
        mdb.models['Model-1'].sketches['__profile__'])"""

    mdb.models['Model-1'].ConstrainedSketch(name='__profile__', sheetSize=1.0)
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
        9.14, 0.0))

    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(9.14, 0.0), point2=(
        18.28, 0.0))

    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.28, 0.0), point2=(
       18.28, 9.14))
    
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(18.28, 9.14), point2=(
        9.14, 9.14))
   
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(9.14, 9.14), point2=(
        0.0, 9.14))
    
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(9.14, 9.14), point2=(
        9.14, 0.0))
   
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 9.14), point2=(
        9.14, 0.0))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(0.0, 0.0), point2=(
        9.14, 9.14))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(9.14, 0.0), point2=(
        18.28, 9.14))
    mdb.models['Model-1'].sketches['__profile__'].Line(point1=(9.14, 9.14), point2=(
        18.28, 0.0))
    mdb.models['Model-1'].Part(dimensionality=TWO_D_PLANAR, name='Part-1', type=
        DEFORMABLE_BODY)
    mdb.models['Model-1'].parts['Part-1'].BaseWire(sketch=
    mdb.models['Model-1'].sketches['__profile__'])
    
    
    
    
    # ====================== Create Material ====================== 
    
    # These variables have now changed 
    # Youngs Modulus (Steel) E = 200 GPa = 200 x 10^9
    # Poisson's Ratio v = 0.3
    # These variables have now changed 
    
    mdb.models['Model-1'].Material(name='Steel')
    mdb.models['Model-1'].materials['Steel'].Elastic(table=((69000000000.0, 0.3), 
        ))
    mdb.models['Model-1'].materials['Steel'].Density(table=((2770.0, ), ))
    # mdb.models['Model-1'].materials['Material-1'].Depvar()
        
        
    # ====================== Create Sections ====================== 
    mdb.models['Model-1'].TrussSection(area=area1, material='Steel', name='Beam1')
    mdb.models['Model-1'].TrussSection(area=area2, material='Steel', name='Beam2')
    mdb.models['Model-1'].TrussSection(area=area3, material='Steel', name='Beam3')
    mdb.models['Model-1'].TrussSection(area=area4, material='Steel', name='Beam4')
    mdb.models['Model-1'].TrussSection(area=area5, material='Steel', name='Beam5')
    mdb.models['Model-1'].TrussSection(area=area6, material='Steel', name='Beam6')
    mdb.models['Model-1'].TrussSection(area=area7, material='Steel', name='Beam7')
    mdb.models['Model-1'].TrussSection(area=area8, material='Steel', name='Beam8')
    mdb.models['Model-1'].TrussSection(area=area9, material='Steel', name='Beam9')
    mdb.models['Model-1'].TrussSection(area=area10, material='Steel', name='Beam10')
    
    # ====================== Assign Sections ====================== 
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
    mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#10 ]', 
    ), ), name='Set-1')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-1'], sectionName='Beam1', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#400 ]', 
        ), ), name='Set-2')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-2'], sectionName='Beam2', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#60 ]', 
        ), ), name='Set-3')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-3'], sectionName='Beam3', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#300 ]', 
        ), ), name='Set-4')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-4'], sectionName='Beam4', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask((
        '[#2000 ]', ), ), name='Set-5')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-5'], sectionName='Beam5', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#808 ]', 
        ), ), name='Set-6')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-6'], sectionName='Beam6', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask((
        '[#1004 ]', ), ), name='Set-7')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-7'], sectionName='Beam7', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#2 ]', 
        ), ), name='Set-8')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-8'], sectionName='Beam8', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#80 ]', 
        ), ), name='Set-9')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-9'], sectionName='Beam9', 
        thicknessAssignment=FROM_SECTION)
    mdb.models['Model-1'].parts['Part-1'].Set(edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask(('[#1 ]', 
        ), ), name='Set-10')
    mdb.models['Model-1'].parts['Part-1'].SectionAssignment(offset=0.0, 
        offsetField='', offsetType=MIDDLE_SURFACE, region=
        mdb.models['Model-1'].parts['Part-1'].sets['Set-10'], sectionName='Beam10', 
        thicknessAssignment=FROM_SECTION)
    
    
    
    
    
    
    
    
    
    # ====================== Create Load Step ====================== 
    mdb.models['Model-1'].rootAssembly.DatumCsysByDefault(CARTESIAN)
    mdb.models['Model-1'].rootAssembly.Instance(dependent=ON, name='Part-1-1', 
        part=mdb.models['Model-1'].parts['Part-1'])
    mdb.models['Model-1'].StaticStep(description='Applied Load', name='Load', 
        previous='Initial')
    mdb.models['Model-1'].fieldOutputRequests['F-Output-1'].setValues(variables=(
        'S', 'U', 'RF', 'CF'))
    del mdb.models['Model-1'].historyOutputRequests['H-Output-1']
        
    # ====================== Create Boundary Conditions ====================== 
    
    
    
    
    mdb.models['Model-1'].rootAssembly.Set(name='Set-1', vertices=
    mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
    ('[#a0 ]', ), ))
    mdb.models['Model-1'].DisplacementBC(amplitude=UNSET, createStepName='Load', 
        distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name=
        'Pinned', region=mdb.models['Model-1'].rootAssembly.sets['Set-1'], u1=0.0, 
        u2=0.0, ur3=UNSET)
    mdb.models['Model-1'].rootAssembly.Set(name='Set-2', vertices=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
        ('[#2 ]', ), ))
        
    # ====================== Create Loads ======================   
    mdb.models['Model-1'].ConcentratedForce(cf2=-445000, createStepName='Load', 
        distributionType=UNIFORM, field='', localCsys=None, name='PointLoad', 
        region=mdb.models['Model-1'].rootAssembly.sets['Set-2'])
    mdb.models['Model-1'].rootAssembly.Set(name='Set-3', vertices=
        mdb.models['Model-1'].rootAssembly.instances['Part-1-1'].vertices.getSequenceFromMask(
        ('[#1 ]', ), ))
    mdb.models['Model-1'].ConcentratedForce(cf2=-445000, createStepName='Load', 
        distributionType=UNIFORM, field='', localCsys=None, name='Load-2', region=
        mdb.models['Model-1'].rootAssembly.sets['Set-3'])
    
            
    # ====================== Meshing ======================   
    mdb.models['Model-1'].parts['Part-1'].setElementType(elemTypes=(ElemType(
    elemCode=T2D2, elemLibrary=STANDARD), ), regions=(
    mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask((
    '[#3fff ]', ), ), ))
    mdb.models['Model-1'].parts['Part-1'].seedEdgeByNumber(constraint=FINER, edges=
        mdb.models['Model-1'].parts['Part-1'].edges.getSequenceFromMask((
        '[#3fff ]', ), ), number=1)
    mdb.models['Model-1'].parts['Part-1'].generateMesh()
    
    # ====================== Create Job ======================   
    mdb.models['Model-1'].rootAssembly.regenerate()
    mdb.Job(atTime=None, contactPrint=OFF, description=
        'Static Analysis of a truss with two point loads', echoPrint=OFF, 
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF, 
        multiprocessingMode=DEFAULT, name='Truss', nodalOutputPrecision=SINGLE, 
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)
        
    # ====================== Submit Job ======================   
    #mdb.jobs['Truss'].submit(consistencyChecking=OFF)
    
    #mdb.jobs['TBEAM'].submit(consistencyChecking=OFF)
    myJob1 = mdb.Job(name='Truss', model='Model-1',)
    myJob1.submit()
    # Wait for the Job to complete. 
    try:
        myJob1.waitForCompletion(6000)
    except AbaqusException, message:
        print "Job timed out", message
    
    
    # ====================== Collect Results ====================== TESTING

    from abaqus import *
    from abaqusConstants import *
    session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=290, 
        height=160)
    session.viewports['Viewport: 1'].makeCurrent()
    session.viewports['Viewport: 1'].maximize()
    from caeModules import *
    from driverUtils import executeOnCaeStartup

    img_folder = 'Images/'
    txt_folder = 'Output/'

    o1 = session.openOdb(
        name='C:/Users/TommyHielscher/Desktop/Benchmark Optimization/10 Bar Truss/Truss.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)

        # Set Camera for deflection image capture
    session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
        CONTOURS_ON_DEF, ))
    session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
        visibleEdges=FEATURE)
    session.printOptions.setValues(vpDecorations=OFF)
    session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
        variableLabel='U', outputPosition=NODAL, refinement=(INVARIANT, 
        'Magnitude'), )
    session.printToFile(fileName=img_folder+'IsoImage_' + str(sol), format=TIFF, canvasObjects=(
        session.viewports['Viewport: 1'], ))
    
    
    # Export data to text file
    session.xyDataListFromField(odb=o1, outputPosition=NODAL, variable=(('U', 
        NODAL, ((INVARIANT, 'Magnitude'), )), ('S', INTEGRATION_POINT, ((INVARIANT, 
        'Mises'), )), ), nodeSets=(" ALL NODES", ))
    
    x0 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 1']
    x1 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 2']
    x2 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 3']
    x3 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 4']
    x4 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 5']
    x5 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 6']
    x6 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 7']
    x7 = session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 8']
    session.writeXYReport(fileName= txt_folder+'abaqus_output_stress' + str(sol) +'.txt', appendMode=OFF, xyData=(x0, x1, x2, x3, x4, x5, 
        x6, x7))
        
    x8 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 1']
    x9 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 2']
    x10 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 3']
    x11 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 4']
    x12 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 5']
    x13 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 6']
    x14 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 7']
    x15 = session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 8']
    session.writeXYReport(fileName= txt_folder+'abaqus_output_def' + str(sol) +'.txt', appendMode=OFF, xyData=(x8, x9, x10, x11, x12, x13, x14, x15))
    
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 8']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 1']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 2']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 3']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 4']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 5']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 6']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 7']
    del session.xyDataObjects['S:Mises (Avg: 75%) PI: PART-1-1 N: 8']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 1']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 2']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 3']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 4']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 5']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 6']
    del session.xyDataObjects['U:Magnitude PI: PART-1-1 N: 7']

    # END OF TESTING
    # ====================== Close the file ====================== 
    mdb.close()
    
    print("Going on to next solution")
    sol += 1
    continue
    
    
        #if sol > 100:  
    #if sol < iterations:
     #   sol += 1
      #  print("Going on to next solution")
       # continue
    
    # End optimization 
    #break