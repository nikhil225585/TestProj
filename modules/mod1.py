import json

class JobConfig:
    def __init__(self, config):
        for key in config:
            setattr(self, key, config[key])


class DataHandler:
    """
        Holds all data handling functions uses JobConfig and s3Client classes
    """

    def __init__(self, config: dict):
        """
        :param  config      :   dictionary holding the job config and s3 dictionary
                glueContext
                spark
        """
        job_config: JobConfig
        self.job_config = JobConfig(config)
