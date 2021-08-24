# names = ["name","xiepeng","age","37"]
#
# w = open("address","w")
# w.write(str(names))
# f=w.read("address")



# from sf_interface.senseface.v43.public_operating.public_common import *
def ord_user_lib_task_cancel_all_video_permissions_delete_task_restart_task_info(host,log,user,password):
    random_str = get_random_name()
    task_name = "人像库" + random_str
    obj_data = TscSC(host,log,user,alarm=True,pre_user=True,pre_user_name=BaseOperation.pre_test_user1,create_video=True,custom_builds={
        "rtsp":{"count":1,"access":["face"],"path":["rtsp://10.9.244.23:8554/lz4-5.264"]}},pre_lib=True,pre_rtsp_typo=6
    )
    obj_data.switch_user(BaseOperation.pre_test_user1,BaseOperation.password)
    photo_info = obj_data.pub_alrm.add_library_task(task_name=task_name,get_alarm=False,stop_stop=True)

