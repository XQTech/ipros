from .models import Config
from .exception_handler import DataUnavailable

class SysConfig(object):

    def __init__(self):
        try:
            self.configDB = Config.objects.all()
        except Config.DoesNotExist:
            raise DataUnavailable('Config not found!', 'Data_Unavailable')
        

    def getStringConfig(self, configKey):
        try:
            return self.configDB.get(key=configKey).value
        except Config.DoesNotExist:
            raise DataUnavailable('Config key: ' + configKey + ' not found!', 'Data_Unavailable')
    
    def getIntConfig(self, configKey):
        try:
            return int(self.configDB.get(key=configKey).value)
        except Config.DoesNotExist:
            raise DataUnavailable('Config key: ' + configKey + ' not found!', 'Data_Unavailable')
    
    def getFloatConfig(self, configKey):
        try:
            return float(self.configDB.get(key=configKey).value)
        except Config.DoesNotExist:
            raise DataUnavailable('Config key: ' + configKey + ' not found!', 'Data_Unavailable')


class ConfigKey(object):

    JIRA_QUERY = "JIRA_QUERY"
    JIRA_ACCOUNT = "JIRA_ACCOUNT"
    JIRA_PASSWORD = "JIRA_PASSWORD"
    JIRA_SERVER = "JIRA_SERVER"
    DOC_FD_NAME = "DOC_FD_NAME"
    DOC_BK_NAME = "DOC_BK_NAME"
    WARN_DUE_DAYS = "WARN_DUE_DAYS"
    INCOMPLETE_BK_ST_ID = "INCOMPLETE_BK_ST_ID"

    class ConfigError(TypeError):
        pass

    class ConfigCaseError(ConfigError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConfigError("Can't change const.%s" % name)
        if not name.isupper():
            raise self.ConfigCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

