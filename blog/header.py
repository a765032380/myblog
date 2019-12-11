class Header:
    u_id: str
    platform: str
    sys_version: str
    device: str
    screen: str
    uuid: str
    version: str
    api_version: str
    token: str
    channel_id: str

    def __init__(self, u_id, platform, sys_version, device, screen, uuid, version, api_version, token, channel_id,
                 network_type):
        self.u_id = u_id
        self.platform = platform  # 平台
        self.sys_version = sys_version  # 系统版本号
        self.device = device  # 设备信息
        self.screen = screen  # 屏幕大小
        self.uuid = uuid  # 设备唯一码
        self.version = version  # app版本
        self.api_version = api_version  # api版本
        self.token = token  # 令牌
        self.channel_id = channel_id  # 渠道
        self.network_type = network_type  # 网络类型
