class InvalidOutputError(Exception):
    def __init__(self):
        return super().__init__('Must be a list of gybe.types.K8sResource')
