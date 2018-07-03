import pcl


def generatePointClouds():

    file_tracker = 0

    for file_name in os.listdir(raw_depth_folder):
        imageDepth = cv2.imread(raw_depth_folder + file_name, 2)

        image_points = [[0,0,0]] * (640 * 480)
        tracker = 0
        for i in range(len(imageDepth)):
            for j in range(len(imageDepth[0])):
                depth_value = float(imageDepth[i][j]) / 10.0
                X = float((i - 347)) * float(depth_value) / float(626.54) #Alan, replace these fx/fy/cx/cy with correct parameters using rostopic echo blahblahblah
        Y = float((j - 225)) * float(depth_value) / float(632)
                image_points[tracker] = [X, Y, depth_value]
                tracker += 1

    pclObject = pcl.PointCloud()
    pclObject.from_array(numpy.array(image_points, dtype=numpy.float32))
    #fil = pclObject.make_statistical_outlier_filter()
    #fil.set_mean_k (50)
    #fil.set_std_dev_mul_thresh (3.0)
    #filteredPclObject = fil.filter()
    print pcd_folder + 'PCDFile' + str(file_tracker) + '.pcd'
    pclObject.to_file(pcd_folder + 'PCDFile' + str(file_tracker) + '.pcd')
    pcl.save(pclObject, pcd_folder + 'PLYFile' + str(file_tracker) + '.ply')
        file_tracker += 1
