def Classify(nItem, k, Items): 
    if(k > len(Items)): 
          
        # k is larger than list 
        # length, abort 
        return "k larger than list length"; 
      
    # Hold nearest neighbors. 
    # First item is distance,  
    # second class 
    neighbors = []; 
  
    for item in Items: 
        
        # Find Euclidean Distance 
        distance = EuclideanDistance(nItem, item); 
  
        # Update neighbors, either adding 
        # the current item in neighbors  
        # or not. 
        neighbors = UpdateNeighbors(neighbors, item, distance, k); 
  
    # Count the number of each 
    # class in neighbors 
    count = CalculateNeighborsClass(neighbors, k); 
  
    # Find the max in count, aka the 
    # class with the most appearances. 
    return FindMax(count); 
