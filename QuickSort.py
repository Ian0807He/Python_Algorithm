def QuickSort(List):
    if len(List)<=1 :
        return List
    return QuickSort([lt for lt in List[1:] if lt < List[0]]) + [List[0]] + QuickSort([ge for ge in List[1:] if ge >= List[0]])
