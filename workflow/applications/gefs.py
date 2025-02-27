from applications.applications import AppConfig
from pygw.configuration import Configuration


class GEFSAppConfig(AppConfig):
    '''
    Class to define GEFS configurations
    '''

    def __init__(self, conf: Configuration):
        super().__init__(conf)

    def _get_app_configs(self):
        """
        Returns the config_files that are involved in gefs
        """
        configs = ['fcst']

        if self.nens > 0:
            configs += ['efcs']

        return configs

    @staticmethod
    def _update_base(base_in):

        base_out = base_in.copy()
        base_out['INTERVAL_GFS'] = AppConfig.get_gfs_interval(base_in['gfs_cyc'])
        base_out['CDUMP'] = 'gefs'

        return base_out

    def get_task_names(self):

        tasks = ['fcst']

        if self.nens > 0:
            tasks += ['efcs']

        return {f"{self._base['CDUMP']}": tasks}
