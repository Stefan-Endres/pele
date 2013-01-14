from minpermdist_stochastic import MinPermDistCluster
from exact_match import ExactMatchCluster
from _minpermdist_policies import TransformAtomicCluster, MeasureAtomicCluster

class MinPermDistAtomicCluster(MinPermDistCluster):
    def __init__(self, permlist=None, **kwargs):
        transform=TransformAtomicCluster()
        measure = MeasureAtomicCluster(permlist=permlist)
        
        MinPermDistCluster.__init__(self, transform=transform, measure=measure, **kwargs)
        
class ExactMatchAtomicCluster(ExactMatchCluster):
    def __init__(self, permlist=None, **kwargs):
        transform=TransformAtomicCluster()
        measure = MeasureAtomicCluster(permlist=permlist)
        
        ExactMatchCluster.__init__(self, transform=transform, measure=measure, **kwargs)