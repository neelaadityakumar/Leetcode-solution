class Solution:
    def kClosest(self, points, k):
        def calc_distance(point):
            return point[0]**2 + point[1]**2
        
        def quickselect(l, r):   
            # pick pivot at random, swap it to the right (random pivot improves performance substantially)
            rand_index = random.randrange(l, r+1)
            points[rand_index], points[r] = points[r], points[rand_index]
            
            # initalize pivot and p
            pivot_distance = calc_distance(points[r])
            p = l
            
            # iterate points in the range [l, r] (non inclusive of r)
            for i in range(l, r):
                # if current point dist <= pivot distance
                if calc_distance(points[i]) <= pivot_distance:
                    # swap point with current p location
                    points[p], points[i] = points[i], points[p]
                    p += 1
            
            # swap our pivot which located in r, to its correct position
            points[p], points[r] = points[r], points[p]
            
            # we want to return closest K points, which means that our p should actually be equal to index of k-1
            if p > k-1: return quickselect(l, p - 1)
            elif p < k-1: return quickselect(p+1, r)
            
            # now we return the first k elements
            return points[:k]
        
        return quickselect(0, len(points) - 1)