#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
from Test_Selenium.common.common_func import *

class ResDefine:
    dft_url_port = '10219'
    dft_url_ssh_port = '10220'

    name_prefix = "UI_"

    pre_res = "{}pre_".format(name_prefix)
    # 业务系统上 目前默认值
    dft_new_user_pwd = '88888888'
    new_pwd = 'admin1234'
    top_dep = "一级部门（可修改名称）"  # 用户部门 默认的一级部门名
    dep_2_ = "{}二级部门".format(pre_res)  # 用户部门 默认的二级部门名
    dep_3_ = "{}三级部门".format(pre_res)  # 用户部门 默认的三级部门名

    dft_role = "系统管理员"  # 4.2 修改 系统管理员 为管理员为bug 20200628
    # 预置普通用户
    pre_com_user = "{}普通用户".format(pre_res)
    # pre_com_user_no = "{}无审核无审批".format(pre_res)
    # pre_com_user_chk = "{}有审核无审批".format(pre_res)
    # pre_com_user_app = "{}有审核有审批".format(pre_res)
    # new
    pre_com_2_user = "{}二级_普通用户".format(pre_res)
    pre_com_2_no_app_user = "{}二级_无审批用户".format(pre_res)
    pre_com_3_user_no_edit = "{}三级_无编辑审核审批".format(pre_res)
    pre_com_3_user_no = "{}三级_无审核审批".format(pre_res)
    # pre_com_user_app = "{}有审核有审批".format(pre_res)
    pre_com_user_no = pre_com_3_user_no
    pre_com_user_chk = pre_com_2_no_app_user
    pre_com_user_app = pre_com_2_user
    # 资源收集 存储key
    store_key = 'SC'
    key_camera = 'camera_names'
    key_camera_group = 'camera_group_'
    key_camera_block = 'camera_block_types'
    key_lib = 'lib_names'
    key_static_lib = 'static_lib_names'
    key_user = 'user_names'
    key_role = 'role_names'
    key_dep = 'dep_names'
    key_task = 'task_names'
    key_region_task = "region_task"
    key_into_lib_task = "into_lib_task"
    key_crowd_task = "crowd_task"
    key_check_repeat = "check_repeat_task"
    # 普通用户角色的最全权限， 调取权限需结合以下获取方法使用 csf

    __right_dict = {'操作导航': {'使用': True}, '数据汇智': {'使用': True}, '个人中心': {'使用': True}, '离线检索': {'使用': True},
                    '身份检索': {'使用': True}, '智能检索': {'使用': True}, '车辆检索': {'使用': True}, '时空过滤': {'使用': True},
                    '融合检索': {'使用': True}, '行人检索': {'使用': True}, '人脸检索': {'使用': True},
                    '布控': {'查看': True, '编辑': True, '审核': True, '审批': True}, '解析管理': {'查看': True, '编辑': True},
                    '任务中心': {'任务调度': True, '基础功能': True}, '卡口': {'使用': True}, '区域碰撞': {'使用': True},
                    '1:1验证': {'使用': True}, '身份库': {'查看': True, '编辑': True}, '布控库': {'查看': True, '编辑': True},
                    '静态库': {'查看': True, '编辑': True}, '视图源管理': {'查看': True, '编辑': False}, '角色管理': {'使用': False},
                    '用户管理': {'查看': True, '编辑': False}, '操作日志': {'查看': True}, '系统设置': {'查看': True, '编辑': True},
                    '地图中心': {'使用': True}}
    # 库define
    pre_lib_alert_1 = '{}pre_one_por'.format(name_prefix)
    pre_lib_static_1 = '{}pre_static_por'.format(name_prefix)
    pre_lib_alert_65 = '{}pre_65_por'.format(name_prefix)

    @staticmethod
    def get_right_dict(need_right=None, remove_right=None):
        """
        csf 取权限 KV
        :param need_right: 需要添加的权限列表, 格式：模块-权限内容 如[操作导航-使用，个人中心-使用]
        :param remove_right: 需要移除的权限，格式同上，
        :return:
        """
        need_right = convert_to_array(need_right)
        remove_right = convert_to_array(remove_right)
        tmp_right_dict = ResDefine.__right_dict
        for right_ in need_right:
            k1, k2 = right_.split('_') if '_' in right_ else right_.split('-')
            tmp_right_dict[k1][k2] = True
        for right_ in remove_right:
            k1, k2 = right_.split('_') if '_' in right_ else right_.split('-')
            tmp_right_dict[k1][k2] = False
        return tmp_right_dict

    @staticmethod
    def get_file(file_name, version_path="v40"):
        """
        获取素材文件使用（统一分配）
        :param version_path: 版本路径
        :param file_name: 文件名
        """
        import platform
        # file_path = os.path.join(home_path, "material", "SenseFace", "API", version_path, file_name)
        # 判断文件是否存在
        if platform.system() == "Windows":
            file_path = os.path.join(r"\\172.20.25.158\public\material", "SenseFace", "API", version_path,
                                     file_name)  # mx 2020.8.21 素材地址改变，原：10.9.244.32
        else:
            file_path = os.path.join(r"/material", "SenseFace", "API", version_path, file_name)
        if not os.path.exists(file_path):
            raise IOError("文件 {} 不存在".format(file_path))
        return file_path

    # 各模块名
    class ModDefine:
        mod_home_page = "首页"
        mod_home_data = "数据汇智"
        mod_home_op = "操作导航"
        mod_search_face = "人脸检索"
        mod_search_ped = "行人检索"
        mod_search_lib = "身份检索"
        mod_search_id = mod_search_lib
        mod_search_int = "融合检索"
        mod_search_com = "智能检索"
        mod_search_veh = "车辆检索"
        mod_search_ts = "时空过滤"
        mod_search_off = "离线检索"
        mod_task = "布控"
        mod_crowd = "人群分析"
        mod_alarm = "告警中心"
        mod_task_center = "任务中心"
        mod_user = "用户管理"
        mod_role = "角色管理"
        mod_lib = "人像库管理"
        mod_camera = "视图源管理"
        mod_op = "操作日志"
        mod_person = "个人中心"
        mod_system = "系统设置"
        mod_logout = "退出"
        mod_analysis = "解析管理"
        mod_view_tool = "照片一比一"
        mod_surveillance = "卡口"
        mod_region = "区域碰撞"
        mod_into_lib = "入库助手"
        mod_tactics = "技战法"
        mod_checkrepeat = "查重"

        page_url_dict = {
            mod_home_data: "/dashboard",
            mod_home_op: "/navigation-operation",
            mod_search_face: "face-search",
            mod_search_ped: "body-search",
            mod_search_lib: "identity-search",
            mod_search_int: "/integration-search",
            mod_search_com: "intelligent-search",
            mod_search_veh: "vehicle",
            mod_search_ts: "timespace",
            mod_search_off: "offline-search",
            mod_task: "control-tasks",
            mod_crowd: "crowd",
            mod_alarm: "alarms/home",
            mod_task_center: "task-center",
            mod_user: "users",
            mod_role: "/roles",
            mod_lib: "library",
            mod_camera: "video-resources",
            mod_op: "opt-logs",
            mod_person: "/personal-center",
            mod_system: "/system-settings",
            mod_analysis: "multiview-process",
            # mod_view_tool: "image-analysis-tools",
            mod_surveillance: "surveillance",
        }

    class ImgDef:
        face_1 = 'one_face.jpg'
        face2_1 = '31.jpg'

        body_1 = '8.jpg'
        body1_1 = '4.jpg'

        face_1_body_2 = '1550627642980.jpg'  # 一脸二体
        face_1_body_more = "one_face_more_body_image.png"  # 一脸多人体
        face_x = 'manyfaces.jpg'  # 多人脸
        car_1 = 'car1.jpg'  # 此图片车牌过于清晰， 会出现无检索图的情况  csf
        car_12 = 'car1_2.jpg'  # 此图片无车牌，可保证有检索图 csf
        no_face = body_1  # 无脸只有人体照片
        mix_img = 'abc.png'
        # 不同格式图片
        fmt_jpeg = 'format_jpeg.jpeg'
        fmt_bmp = 'format_bmp.bmp'
        fmt_gif = 'format_gif.gif'
        fmt_png = "format_png.png"
        fmt_BMP = "format_BMP_format.BMP"
        fmt_JPEG = "format_JPEG_format.JPEG"
        fmt_JPG = "format_JPG.JPG"
        fmt_PNG = "format_PNG_format.PNG"
        fmt_GIF = "format_GIF.GIF"
        fmt_jpg = face_1

        vague_more_face_body = "vague_more_face_body_image.png"  # 模糊多人脸人体
        vague_face_body = "vague_face_body_image.png"  # 模糊单人脸人体

        size_39 = ''
        size_40 = ''
        size_41 = ''

        size_79 = '0827.jpg'  # size 4M以上8M以下风景 图片
        size_80 = 'ckm_8.0M.bmp'  # size 8M 图片
        size_81 = 'face_exceed_8M.jpg'  # size 大于8M 图片

        not_img = 'feature_qjh.txt'  # 'blank.zip'
        scenery_img = "5.jpg"  # 风景
        archives_img = "09.43.53[M][0@0][1].jpg"
        no_face_no_body_clear = "no_face_no_body_clear.png"  # 无人脸 无人体 清晰图片
        one_pic_zip = '7452004.zip'
        Lz_65_zip = 'lz_65.zip'
        Lz_feature_24802 = 'lz_feature_24802.txt'
        Lz_feature_24702 = 'lz_feature_24702.txt'
        Lz_feature_24602 = 'lz_feature_20181017_10-53-23.txt'
        Lz_feature_24602_new = 'feature_20190925_20-46-30_24602.txt'
        lz_id_zip = 'lz_id.zip'  # 总共5张
        ok_1_zip = 'ok_1.zip'  # 总共5张
        three_doc_zip = 'three_doc.zip'  # 多级别
        error_1_zip = 'error_1.zip'  # 全部导入失败的图片,共4张
        error_nor_zip = 'error_nor.zip'  # 3张导入失败的图片，1张正常图片,共4张
        lz_hasexceed_8M_zip = 'lz_hasexceed_8M.zip'  # zip包中有1张超过8M的图片文件,2张正常图片
        lz_Irregularity_zip = 'lz_Irregularity.zip'  # zip包中部分图片文件名不规则,总共2张
        lz_hasother_zip = 'lz_hasother.zip'  # zip包中有非图片文件,总共2张图片，1个excel
        exceed_200M_zip = 'exceed_200M.zip'  # zip包超过200M，总共2万多张
        single_face = "1557834587830.jpg"
        single_body = "ex.jpg"
        poi_file = "广东省深圳市.txt"
        lz_inter_1 = "lz_inter_1.zip"  # 查重使用的zip,共5张
        lz_inter_2 = "lz_inter_2.zip"  # 查重使用的zip,共14张

        plate_no = '粤B3FW61'  # 车牌号, 在car1视频源中 有
        rtsp_xls = "rtsp_three_new_ui.xlsx"  # "camera_rtsp_import.xlsx"
        block_xls = "视频源区块信息导入_void.xls"


class CameraDefine:
    name_pre = ResDefine.name_prefix
    camera_top_dep = "一级部门（可修改名称）"
    camera_del_dep = "已删除视频源"
    camera_no_dep = "未分组视频源"
    name_test = '{}_cam_'.format(name_pre)
    pre_camera_group = '{}pre_'.format(name_pre)
    pre_camera_group_face = '{}face'.format(pre_camera_group)
    pre_camera_group_ped = '{}ped'.format(pre_camera_group)
    pre_camera_group_face_ped = '{}face_ped'.format(pre_camera_group)
    pre_camera_group_car = '{}car'.format(pre_camera_group)
    pre_camera_group_crowd = '{}crowd'.format(pre_camera_group)
    pre_camera_group_alarm = '{}alarm'.format(pre_camera_group)
    pre_camera_group_search = '{}search'.format(pre_camera_group)

    def_camera_dict = {
        'face': ['人脸', pre_camera_group_face],
        'ped': ['结构化', pre_camera_group_ped],
        'face_ped': ['人脸人体联合', pre_camera_group_face_ped],
        'crowd': [['人群', '结构化'], pre_camera_group_crowd],  # mx 2020.8.28 ,预置人群视频源添加‘结构化’接入
        'car': ['结构化', pre_camera_group_car],
        'alarm': ['人脸', pre_camera_group_alarm],
        'search': [['人脸', '结构化'], pre_camera_group_search],
    }

    test_server_ip = {
        "18": "10.9.244.18:10219", "72": "10.111.32.72:10219", "80": "10.111.32.80:10219",
        "20": "10.9.242.20:10219", "39": "10.9.242.39:10219"}
    # 批量导入的视频源模板名称列的列名
    name_cols_title_in_temple = {"RTSP": "视频源名称", "抓拍机": "视频源名称", "GB28181": "视频源名称"}
    # 批量导入的视频源模板path列的列名
    path_cols_title_in_temple = {"RTSP": "网络地址URL", "抓拍机": "IP地址", "GB28181": "设备ID(必填)"}
    # 批量导入的视频源模板path列的列名
    # device_code_cols_title_in_temple = {"抓拍机": "设备ID(必填)", "摄像机": "设备ID(必填)",
    #                                     "GB28181": "设备ID(必填)"}
    _test_server_ip_prefix_list = ["10.9.242.*", "10.9.244.*", "10.111.32.*"]
    # 素材列表
    _material_file_list = []
    _rtsp_times = 0

    # 清理环境预期errorCOde
    teardown_code = ["0", "400001", "100001", "030004040002", "030004020005", "401003", "403008"]

    # 固定创建，不可操作的   直流摄像机 rtsp协议
    prefix = ResDefine.name_prefix
    _pre_fixed_rtsp_videos = {

        # 人脸接入(index:0-2)
        "{}pre_face_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz1-1.264",
        "{}pre_face_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz1-2.264",
        "{}pre_face_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz1-3.264",

        # 人体接入(index:3-5)
        "{}pre_body_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz3-1.264",
        "{}pre_body_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz3-2.264",
        "{}pre_body_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz3-3.264",

        # 人脸、人体接入(index:6-8)
        "{}pre_both_face_body_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz5-15.264",
        "{}pre_both_face_body_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz5-14.264",
        "{}pre_both_face_body_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz5-13.264",

        # 人群接入(index:9-12)
        # "{}pre_crowd_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz5-1.264",
        # "{}pre_crowd_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz5-2.264",
        # "{}pre_crowd_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz5-3.264",
        "{}pre_crowd_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz5-21.264",
        "{}pre_crowd_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz5-22.264",
        "{}pre_crowd_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz5-23.264",

        # 检索专用(index:12-20)
        "{}pre_search_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz5-1.264",
        "{}pre_search_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz5-2.264",
        "{}pre_search_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz5-3.264",
        # "{}pre_search_rtsp_4".format(name_pre): "rtsp://10.9.244.23:8554/lz5-11.264",
        # "{}pre_search_rtsp_5".format(name_pre): "rtsp://10.9.244.23:8554/lz5-12.264",
        # "{}pre_search_rtsp_6".format(name_pre): "rtsp://10.9.244.23:8554/lz4-3.264",
        # "{}pre_search_rtsp_7".format(name_pre): "rtsp://10.9.244.23:8554/lz4-2.264",
        # "{}pre_search_rtsp_8".format(name_pre): "rtsp://10.9.244.23:8554/lz4-1.264",

        # 告警专用(index:20-24)
        "{}pre_alarm_rtsp_1".format(name_pre): "rtsp://10.9.244.23:8554/lz5-gaojin1.264",
        "{}pre_alarm_rtsp_2".format(name_pre): "rtsp://10.9.244.23:8554/lz5-gaojin2.264",
        "{}pre_alarm_rtsp_3".format(name_pre): "rtsp://10.9.244.23:8554/lz5-gaojin3.264",
        # "{}pre_alarm_rtsp_4".format(name_pre): "rtsp://10.9.244.23:8554/lz5-gaojin4.264",

        # 车辆专用(index:24-27)
        "{}pre_car_rtsp_1".format(name_pre): "rtsp://10.9.242.24:554/44030354001320000398.264",
        "{}pre_car_rtsp_2".format(name_pre): "rtsp://10.9.242.24:554/44030354001320000399.264",
        "{}pre_car_rtsp_3".format(name_pre): "rtsp://10.9.242.24:554/44030354001320000400.264"

    }
    # 固定创建，可操作的 直流摄像机 rtsp协议
    operable_rtsp_videos = {

        # 仅接入、取消接入
        "pre_op_access_rtsp_1": "rtsp://10.9.244.23:8554/lz1-4.264",  # 只接人脸，请不要接入其它
        "pre_op_access_rtsp_2": "rtsp://10.9.244.23:8554/lz3-4.264",  # 只接人体，请不要接入其它
        "pre_op_access_rtsp_3": "rtsp://10.9.244.23:8554/lz4-4.264",
        "pre_op_access_rtsp_4": "rtsp://10.9.244.23:8554/lz5-4.264",
        "pre_op_access_rtsp_5": "rtsp://10.9.244.23:8554/lz1-5.264",
        "pre_op_access_rtsp_6": "rtsp://10.9.244.23:8554/lz3-5.264",
        "pre_op_access_rtsp_7": "rtsp://10.9.244.23:8554/lz4-5.264",

        # 随便蹂虐
        "pre_op_rtsp_1": "rtsp://10.9.244.23:8554/lz5-5.264",
        "pre_op_rtsp_2": "rtsp://10.9.244.23:8554/lz5-11.264",
        "pre_op_rtsp_3": "rtsp://10.9.244.23:8554/lz5-12.264",
        "pre_op_rtsp_4": "rtsp://10.9.244.23:8554/lz4-3.264",
        # "pre_op_rtsp_2": "rtsp://10.9.244.23:8554/lz5-sy1.264",
        # "pre_op_rtsp_3": "rtsp://10.9.244.23:8554/lz5-sy2.264",
        # "pre_op_rtsp_4": "rtsp://10.9.244.23:8554/lz5-sy3.264",
        "pre_op_rtsp_5": "rtsp://10.9.244.23:8554/lz5-15.264",

        # 车辆专用
        "pre_op_car_rtsp_1": "rtsp://10.9.244.23:8554/lz4-pre.264",
        "pre_op_car_rtsp_2": "rtsp://10.9.242.24:554/44030354001320000378.264",
        "pre_op_car_rtsp_3": "rtsp://10.9.242.24:554/44030354001320000378-1.264"

    }

    # 　直流摄像机　onvif协议
    _onvif_params = [
        # 大华
        {"userName": "test", "password": "admin2018", "host": "10.9.189.31", "port": 80, "sourceId": 25,
         "resourceTypeId": 5},  # 默认http协议端口,
        {"userName": "test", "password": "admin2018", "host": "10.9.189.33", "port": 80, "sourceId": 25,
         "resourceTypeId": 5},  # 默认http协议端口
        {"userName": "test", "password": "admin1234", "host": fail_ip_port().split(":")[0],
         "port": fail_ip_port().split(":")[1], "sourceId": 25,
         "resourceTypeId": 5}  # 模拟onvif
    ]
    # 平台摄像机_gb28181
    _gb28181_times = 0
    _gb28181_params = [
        # 人脸
        {"deviceCode": "34020000001330000013", "resourceTypeId": 6, "sourceId": 7, "sourceName": "GB28181",
         "sip": {"platformId": "", "sipPlayBack": 1, "gb28181Item": {"registerWay": 1}}
         },
        # 人体
        {"deviceCode": "34020000000240000002", "resourceTypeId": 6, "sourceId": 7, "sourceName": "GB28181",
         "sip": {"platformId": "", "sipPlayBack": 1, "gb28181Item": {"registerWay": 1}}
         },
        # 无人脸、人体,模拟gb
        {"deviceCode": "34020000001360000001", "resourceTypeId": 6, "sourceId": 7, "sourceName": "GB28181",
         "sip": {"platformId": "", "sipPlayBack": 1, "gb28181Item": {"registerWay": 1}}
         },
    ]
    _gb28181_params_ = lambda self: {"deviceCode": get_mix_str_num(), "resourceTypeId": 6, "sourceId": 7,
                                     "sourceName": "GB28181",
                                     "sip": {"platformId": "", "sipPlayBack": 1, "gb28181Item": {"registerWay": 1}}
                                     }
    # 　平台摄像机　阿里云平台
    _aliyun_params = [
        {
            "sourceTypeRes": [2, 26], "host": fail_ip_port().split(":")[0], "sourceId": 26,
            "deviceCode": random_str_re('[0-9]{20,20}'),
            "resourceTypeId": 4, "port": "3000", "userName": "admin", "password": "admin2018", "face": True,
            "sip": {"gat1400Item": {}, "gb28181Item": {"info": [{}]}, "platformId": "", "sipPlayBack": 1},
            "replayPlatformId": None, "replayId": None
        }
    ]
    # 直流抓拍机配置，海康
    _haikang_capture_params = [
        # 海康
        {"userName": "admin", "password": "admin1234", "host": "192.168.2.82", "port": 8000, "sourceId": 1,
         "resourceTypeId": 3},
        {"userName": "admin", "password": "admin1234", "host": fail_ip_port().split(":")[0],
         "port": fail_ip_port().split(":")[1], "sourceId": 1, "resourceTypeId": 3}  # 模拟假抓拍机

    ]

    # 平台抓拍机配置，GAT1400
    _gat1400_capture_params = [
        {
            "sourceTypeRes": [4, 20], "sourceId": 20, "deviceCode": random_str_re('[0-9]{20,20}'), "resourceTypeId": 7,
            "sip": {"gat1400Item": {}, "gb28181Item": {"info": [{}]}, "platformId": "", "sipPlayBack": 1},
            "replayPlatformId": None, "replayId": None
        }

    ]
    _pre_other_video_names = [
        "pre_video_onvif",  # 直连摄像机onvif协议
        "pre_video_gb_face",  # 平台接入摄像机gb人脸
        "pre_video_gb_body",  # 平台接入摄像机gb结构化
        "pre_video_aliyun",  # 平台接入摄像机(阿里云)
        "pre_video_capture",  # 直连抓拍机
        "pre_video_gat1400_capture"  # 平台接入抓拍机GAT1400
    ]
    # 预置视频源分组（不可编辑、删除）
    _pre_video_group_times = 0
    pre_video_group = [
        "sf_pre_group_1", "sf_pre_group_2", "sf_pre_group_3", "sf_pre_group_4", "sf_pre_group_5",
        "sf_pre_group_6", "sf_pre_group_7", "sf_pre_group_8", "sf_pre_group_9", "sf_pre_group_0"]
    # 预置假的RTSP视频源名称（默认放在sf_pre_rtsp_0分组）
    _pre_fake_rtsp_video_times = 0
    pre_fake_rtsp_videos = [
        "sf_pre_rtsp_1", "sf_pre_rtsp_2", "sf_pre_rtsp_3", "sf_pre_rtsp_4", "sf_pre_rtsp_5",
        "sf_pre_rtsp_6", "sf_pre_rtsp_7", "sf_pre_rtsp_8", "sf_pre_rtsp_9", "sf_pre_rtsp_0"]
    # 预置假的GB28181视频源名称（默认放在sf_pre_rtsp_0分组）
    _pre_fake_gb28181_video_times = 0
    pre_fake_gb28181_videos = [
        "sf_pre_gb28181_1", "sf_pre_gb28181_2", "sf_pre_gb28181_3", "sf_pre_gb28181_4", "sf_pre_gb28181_5",
        "sf_pre_gb28181_6", "sf_pre_gb28181_7", "sf_pre_gb28181_8", "sf_pre_gb28181_9", "sf_pre_gb28181_0"]
    # 预置人像库（默认空库）
    _pre_library_times = 0
    pre_library = [
        "sf_pre_library_11", "sf_pre_library_2", "sf_pre_library_3", "sf_pre_library_4", "sf_pre_library_5",
        "sf_pre_library_6", "sf_pre_library_7", "sf_pre_library_8", "sf_pre_library_9", "sf_pre_library_0"]

    # 摄像头综合信息
    _pre_coordinate_info = [
        {
            'name': '中国工商银行(深圳深港支行)',
            'address': '宝安北路2051号深圳国际商品交易大厦1层',
            'latitude': '22.560802499432',
            'longitude': '114.10887028676',
            'region': '罗湖区'
        },
        {
            'name': '泊林花园',
            'address': '水贝二路38',
            'latitude': '22.572067147168',
            'longitude': '114.12530631004',
            'region': '罗湖区'
        },
        {
            'name': '必胜清洁用品有限公司',
            'address': '深圳市宝安区捷和工业城e栋4楼',
            'latitude': '22.687935054594',
            'longitude': '113.96827301347',
            'region': '宝安区'
        },
        {
            'name': '大梅沙国际水上运动中心-B区',
            'address': '深圳盐田区盐梅路89号大梅沙国际水上运动中心内',
            'latitude': '22.59792698245',
            'longitude': '114.31219866007',
            'region': '盐田区'
        },
        {
            'name': '钢球批发',
            'address': '大宗柌路8-2号附近',
            'latitude': '22.736351440265',
            'longitude': '113.83589626225',
            'region': '宝安区'
        },
        {
            'name': '佳家修鞋店',
            'address': '深圳市福田区景密村商业街6号',
            'latitude': '22.555694078201',
            'longitude': '114.03797899716',
            'region': '福田区'
        },
        {
            'name': '中国银行(振业城支行)',
            'address': '广东省深圳市龙岗区横岗街道六约振业城4号商铺首层',
            'latitude': '22.635081610523',
            'longitude': '114.18111790294',
            'region': '龙岗区'
        },
        {
            'name': '塘头又一村-24号楼',
            'address': '广东省深圳市宝安区中心区塘头大道塘头又一村24号楼',
            'latitude': '22.654814048715',
            'longitude': '113.91597808921',
            'region': '宝安区'
        },
        {
            'name': '安达汽车服务中心(水贝二路)',
            'address': '水贝国际珠宝城',
            'latitude': '22.571660273518',
            'longitude': '114.12390281505',
            'region': '罗湖区'
        },
        {
            'name': '名艺专业美发机构',
            'address': '广东省深圳市龙岗区湖田路70号',
            'latitude': '22.771821127833',
            'longitude': '114.31207852342',
            'region': '龙岗区'
        },
        {
            'name': '博弛油泵',
            'address': '广东省深圳市龙岗区凤岐路12号富安大道与凤歧路交叉口',
            'latitude': '22.683519602423',
            'longitude': '114.10860230301',
            'region': '龙岗区'
        },
        {
            'name': '鹏兴胶袋厂',
            'address': '石岩北环路源泉百货正对面',
            'latitude': '22.68317044444',
            'longitude': '113.9459473859',
            'region': '宝安区'
        },
        {
            'name': '新感觉专业烫染店(科技路店)',
            'address': '广东省深圳市坪山区科技路1-3号附近',
            'latitude': '22.71248868248',
            'longitude': '114.40013587325',
            'region': '坪山区'
        },
        {
            'name': '成都面馆(旺棠店)',
            'address': '新高路123-19号',
            'latitude': '22.585198601404',
            'longitude': '113.948949754',
            'region': '南山区'
        },
        {
            'name': '女子美妆美甲',
            'address': '盛平南路32号',
            'latitude': '22.729926375138',
            'longitude': '114.25516922876',
            'region': '龙岗区'
        },
        {
            'name': '共青团(龙华办事处)',
            'address': '观澜大道238号附近',
            'latitude': '22.675304558587',
            'longitude': '114.03697952229',
            'region': '龙华区'
        },
        {
            'name': '嘉悦酒店(西环路店)',
            'address': '广东省深圳市宝安区福和路西4巷5号',
            'latitude': '22.756617754452',
            'longitude': '113.80354829149',
            'region': '宝安区'
        }
    ]

    def generate_camera_info(self, camera_type, camera_use='face', fake=True):
        """
        返回视频源 信息
        :param camera_type: 视频源类型规格，rtsp-gb-haikang-ali-onv-1400 6种
                                          rtsp又分为和 rtsp和 rtsp-pre(禁止用例使用，留给预置使用) ,
                                            rtsp-op 又分为3种， rtsp-op-car rtsp-op-only(只接入不能修改)及rtsp-op
        :param camera_use: 用途，主要针对rtsp和gb设置， 目前 有face ped car only 4个
        :return:
        """
        pre_num_lmt = 3
        camera_type = camera_type.lower()
        camera_use = camera_use.lower()
        if 'rtsp' in camera_type:
            if fake:
                return fail_ip_port(prefix_rtsp=True)
            if 'pre' not in camera_type:  # 可操作的
                cam_dict = self.operable_rtsp_videos
                if 'car' in camera_use:
                    use_keyword = 'pre_op_car_rtsp_'
                elif 'only' in camera_use:
                    use_keyword = 'pre_op_access_rtsp_'
                else:
                    use_keyword = 'pre_op_rtsp_'
                filter_cam_dict = {x: y for x, y in cam_dict.items() if use_keyword and use_keyword in x}
                return list(filter_cam_dict.values())[random.randint(0, len(filter_cam_dict) - 1)]
            else:  # 用于预置取
                cam_dict = self._pre_fixed_rtsp_videos
                cam_dict_return = {}
                use_keyword_dict = {
                    'face': 'pre_face_rtsp',
                    'ped': 'pre_body_rtsp',
                    'face_ped': 'pre_both_face_body_rtsp',
                    'crowd': 'pre_crowd_rtsp_',
                    'car': 'pre_car_rtsp',
                    # # 功能
                    'alarm': 'pre_alarm_rtsp',
                    'search': 'pre_search_rtsp',
                }
                use_keyword = use_keyword_dict.get(camera_use, None)
                # if camera_use == 'face':
                #     use_keyword = 'pre_face_rtsp'
                # if camera_use == 'ped':
                #     use_keyword = 'pre_body_rtsp'
                # if camera_use == 'face_ped':
                #     use_keyword = 'pre_both_face_body_rtsp'
                # if camera_use == 'crowd':
                #     use_keyword = 'pre_crowd_rtsp_'
                # if camera_use == 'car':
                #     use_keyword = 'pre_car_rtsp'
                # # 功能
                # if camera_use == 'alarm':
                #     use_keyword = 'pre_alarm_rtsp'
                # if camera_use == 'search':
                #     use_keyword = 'pre_search_rtsp'
                # cam_dict_return.update({x: y for x, y in list(cam_dict.keys()) if use_keyword and use_keyword in x})
                cam_dict_return.update({x: cam_dict[x] for x in
                                        [x for x in list(cam_dict.keys()) if use_keyword and use_keyword in x][
                                        :pre_num_lmt]})
                return cam_dict_return
        elif 'gb' in camera_type:
            cam_lst = self._gb28181_params
            if fake:
                return self._gb28181_params_()
            if camera_use == 'face':
                return cam_lst[0]
            elif camera_use == 'ped':
                return cam_lst[1]
            else:
                return cam_lst[2]
        elif 'ali' in camera_type:
            cam_lst = self._aliyun_params
            return cam_lst[random.randint(0, len(cam_lst) - 1)]
        elif 'haikai' in camera_type or "海康" in camera_type or 'hk' in camera_type:
            cam_lst = self._haikang_capture_params
            if not fake:
                return cam_lst[0]
            else:
                return cam_lst[1]
        elif '1400' in camera_type:
            cam_lst = self._gat1400_capture_params
            return cam_lst[random.randint(0, len(cam_lst) - 1)]
        elif 'onv' in camera_type:
            cam_lst = self._onvif_params
            if fake:
                return cam_lst[-1]
            return cam_lst[random.randint(0, len(cam_lst) - 2)]
        else:
            return None


class TaskDefine:
    preset_accurate_fuzzy_task_name = "{}pre精准模糊布控_请勿终止和编辑".format(ResDefine.name_prefix)
    preset_task_name = "{}pre精准布控_请勿终止和编辑".format(ResDefine.name_prefix)
    preset_accurate_alarm_threshold = "80.8"
    preset_threshold = "10"
    lib_65 = ResDefine.pre_lib_alert_65
    lib_1 = ResDefine.pre_lib_alert_1
    prefix_name = "{}task".format(ResDefine.name_prefix)
    pre_threshold_value = "2"  # 系统设置阈值下限
    task_time_value = "60"  # 系统设置任务持续时长
    search_scsope_value = "5000"  # 系统设置人体检索范围


class CheckRepeat:
    cluster_task_name = "{}pre_查重聚类任务".format(ResDefine.name_prefix)
    compare_lib_task_name = "{}pre_查重库间比对任务".format(ResDefine.name_prefix)


define = ResDefine
define_camera = CameraDefine
