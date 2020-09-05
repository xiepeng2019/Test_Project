import time

html_head = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!-- saved from url=(0058)file:///Z:/pro_python_js/Automated-Test-master/result.html -->
<html xmlns="http://www.w3.org/1999/xhtml"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>测试报告</title>
    <meta name="generator" content="HTMLTestRunner 0.8.2">

    <link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.0/css/bootstrap.min.css">
    <script src="http://cdn.bootcss.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script src="http://apps.bdimg.com/libs/Chart.js/0.2.0/Chart.min.js"></script>
    <!-- <link href="https://cdn.bootcss.com/echarts/3.8.5/echarts.common.min.js" rel="stylesheet">   -->


<style type="text/css" media="screen">
body        { font-family: verdana, arial, helvetica, sans-serif; font-size: 80%; }
table       { font-size: 100%; }
pre         {  }
/* -- heading ---------------------------------------------------------------------- */
h1 {
	font-size: 16pt;
	color: gray;
}
.heading {
    font-size: 12px;
    margin-top: 0ex;
    margin-bottom: 1ex;
	margin-left: 10px;
}
.heading .attribute {
    font-size: 12px;
    margin-top: 1ex;
    margin-bottom: 0;
}
.heading .description {
    font-size: 12px;
    margin-top: 4ex;
    margin-bottom: 6ex;
}
/* -- css div popup ------------------------------------------------------------------------ */
a.popup_link {
}
a.popup_link:hover {
    color: red;
}
.popup_window {
    display: none;
    position: relative;
    left: 0px;
    top: 0px;
    /*border: solid #627173 1px; */
    font-family: "Lucida Console", "Courier New", Courier, monospace;
    text-align: left;
    font-size: 12pt;
    width: 1300px;
}
}
/* -- report ------------------------------------------------------------------------ */
#show_detail_line {
    margin-top: 3ex;
    margin-bottom: 1ex;
    margin-left: 10px;
}
#result_table {
    width: 95%;
    border-collapse: collapse;
    border: 1px solid #777;
    margin-left: 10px;
}
#header_row {
    font-weight: bold;T
    color: #606060;
    background-color: #f5f5f5;
    border-top-width: 10px;
    border-color: #d6e9c6;
	font-size: 12px;
}
#result_table td {
    font-size:10px
    border: 1px solid #f5f5f5;
    padding: 2px;
}
#total_row  { font-weight: bold; }
.passClass  { background-color: #d6e9c6; }
.failClass  { background-color: #faebcc; }
.errorClass { background-color: #ebccd1; }
.passCase   { color: #6c6; }
.failCase   { color: #c60; font-weight: bold; }
.errorCase  { color: #c00; font-weight: bold; }
.hiddenRow  { display: none; }
.testcase   { margin-left: 2em; }
/* -- ending ---------------------------------------------------------------------- */
#ending {
}
/* -- chars ---------------------------------------------------------------------- */
.testChars {margin-left: 150px; font-size:10px; text-align:center;}
.btn-info1 {
    color: #fff;
    background-color: #28B463;
    border-color: #d6e9c6;
}
.btn-info2 {
    color: #fff;
    background-color: #D4AC0D;
    border-color: #faebcc;
}
.btn-info22 {
    color: #fff;
    background-color: #00F0F0;
    border-color: #faebcc;
}
.btn-info3 {
    color: #fff;
    background-color: #D35400;
    border-color: #ebccd1;
}
</style>

</head>
<body>
<script language="javascript" type="text/javascript"><!--
output_list = Array();
/* level - 0:Summary; 1:Failed; 2:All */
function showCase(level) {
    trs = document.getElementsByTagName("tr");
    for (var i = 0; i < trs.length; i++) {
        tr = trs[i];
        id = tr.id;
        if (id.substr(0,2) == 'ft') {
            if (level < 1) {
                tr.className = 'hiddenRow';
            }
            else {
                tr.className = '';
            }
        }
        if (id.substr(0,2) == 'pt') {
            if (level > 1) {
                tr.className = '';
            }
            else {
                tr.className = 'hiddenRow';
            }
        }
    }
}
function showClassDetail(cid, count) {
    var id_list = Array(count);
    var toHide = 1;
    for (var i = 0; i < count; i++) {
        tid0 = 't' + cid.substr(1) + '.' + (i+1);
        tid = 'f' + tid0;
        tr = document.getElementById(tid);
        if (!tr) {
            tid = 'p' + tid0;
            tr = document.getElementById(tid);
        }
        id_list[i] = tid;
        if (tr.className) {
            toHide = 0;
        }
    }
    for (var i = 0; i < count; i++) {
        tid = id_list[i];
        if (toHide) {
            document.getElementById('div_'+tid).style.display = 'none'
            document.getElementById(tid).className = 'hiddenRow';
        }
        else {
            document.getElementById(tid).className = '';
        }
    }
}
function showTestDetail(div_id){
    var details_div = document.getElementById(div_id)
    var displayState = details_div.style.display
    // alert(displayState)
    if (displayState != 'block' ) {
        displayState = 'block'
        details_div.style.display = 'block'
    }
    else {
        details_div.style.display = 'none'
    }
}
function html_escape(s) {
    s = s.replace(/&/g,'&amp;');
    s = s.replace(/</g,'&lt;');
    s = s.replace(/>/g,'&gt;');
    return s;
}
/* obsoleted by detail in <div>
function showOutput(id, name) {
    var w = window.open("", //url
                    name,
                    "resizable,scrollbars,status,width=800,height=450");
    d = w.document;
    d.write("<pre>");
    d.write(html_escape(output_list[id]));
    d.write("\n");
    d.write("<a href='javascript:window.close()'>close</a>\n");
    d.write("</pre>\n");
    d.close();
}
*/
--></script>
"""
html_body_1 = """<div class="heading">
<h1>测试报告</h1>
<p class="attribute"><strong>开始时间:</strong> {0}</p>
<p class="attribute"><strong>结束时间:</strong> {1}</p>
<p class="attribute"><strong>测试耗时:</strong> {2}</p>
<p class="attribute"><strong>运行状态:</strong> Pass {3}</p>

<p class="description">用例执行详情:：</p>
</div>
"""

html_body_11 = """

<div style="float:left; margin-left: 10px; font-size:12px">
	<p> 测试用例结果比 </p>
	<a class="btn btn-xs btn-info1">-Pass-{0}-</a><br>
	<a class="btn btn-xs btn-info2">-Faild-{1}-</a><br>
	<a class="btn btn-xs btn-info22">-Fail-retry-{2}-</a><br>
	<a class="btn btn-xs btn-info1">-Fail-retry-pass-{3}--</a><br>
	<a class="btn btn-xs btn-info3">-Error-{4}-</a><br>
</div>

<div class="testChars" style="center">
	<canvas id="myChart" width="250" height="250" style="width: 250px; height: 250px;"></canvas>
</div>


<p id="show_detail_line" style="margin-left: 16px; font-size:12px">Show
<a href="javascript:showCase(0)" class="btn btn-xs btn-primary">Summary</a>
<a href="javascript:showCase(1)" class="btn btn-xs btn-danger">Failed</a>
<a href="javascript:showCase(2)" class="btn btn-xs btn-info">All</a>
</p>

<table id="result_table">
<colgroup>
<col align="left">
<col align="right">
<col align="right">
<col align="right">
<col align="right">
<col align="right">
</colgroup>
<tbody><tr id="header_row" class="panel-title">
    <td>Test Group/Test case</td>
    <td>Count</td>
    <td>Pass</td>
    <td>Fail</td>
    <td>Error</td>
    <td>View</td>
</tr>
"""

html_body_loop = """

<tr class="{0}">
    <td>{1}</td>
    <td>{2}</td>
    <td>{3}</td>
    <td>{4}</td>
    <td>{5}</td>
    <td><a href="javascript:showClassDetail('c{6}',{2})">详情</a></td>
</tr>
"""

html_body_loop_sub = """

<!-- <tr id="{6}" class="{4} hiddenRow"> -->
<tr id="{6}" class="hiddenRow" >
    <td class="none"><div class="testcase">{1}</div></td>
    <td colspan="5" align="center">
    <!--css div popup start-->
    <a class="popup_link" onfocus="this.blur();" href="javascript:showTestDetail(&#39;div_{6}&#39;)">
        {3}</a>
    <div id="div_{6}" class="popup_window" style="display: none; width:100%;">
        <div style="text-align: right; color:red;cursor:pointer">
        <a onfocus="this.blur();" onclick="document.getElementById('div_{6}').style.display = 'none' ">
           [关闭]</a>
        </div>
        <pre>
{0}：{2}
        </pre>
    </div>
    <!--css div popup end-->
    </td>
</tr>"""

html_body_count = """
<tr id="total_row">
    <td>Total</td>
    <td>{3}</td>
    <td class="text text-success">{0}</td>
    <td class="text text-danger">{1}</td>
    <td class="text text-warning">{2}</td>
    <td>&nbsp;</td>
</tr>"""

html_end = """

</tbody></table>

<div id="ending">&nbsp;</div>

    <script type="text/javascript">
var data = [
	{
	    name: 'error',
		value: %(error)s,
		color: "#D35400",
		label: "Error",
		labelColor: 'white',
		labelFontSize: '16',
		text: "error"
	},
	{
	    name: 'fail',
		value : %(fail)s,
		color : "#D4AC0D",
		label: "Fail",
		labelColor: 'white',
		labelFontSize: '16',
		text: "fail"
	},
	{
	    name: 'fail_retry_pass',
		value : %(fail_retry_pass)s,
		color : "#00F0F0",
		label: "fail_retry_pass",
		labelColor: 'white',
		labelFontSize: '16',
		text: "fail_retry_pass"
	},
	{
	    name : 'pass',
		value : %(Pass)s,
		color : "#28B463",
		label : "Pass",
		labelColor: 'white',
		labelFontSize: '16',
		text: "Pass"
	}
]
var newopts = {
     animationSteps: 100,
 		animationEasing: 'easeInOutQuart',
}
//Get the context of the canvas element we want to select
var ctx = document.getElementById("myChart").getContext("2d");
var myNewChart = new Chart(ctx).Pie(data,newopts);
</script>
"""


def get_tst_log(log_path):
    with open(log_path, 'r', encoding='utf-8') as e:
        return e.read()


def generate_report(run_result, time_dict, report_name=None):
    report_name = report_name or 'report/report_{}.html'.format(time.strftime('%Y-%m-%d_%H%M%S', time.localtime()))
    tst_data = {
        "main_user_role": {
            'UserDep': {'script_author': 'csf',
                        'test_case': 'SC_user_001',
                        'test_error': 'Traceback (most recent call last):\n'
                                      '  File '
                                      '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                      'line 47, in run\n'
                                      '    self.try_catch("测试体", self.action)\n'
                                      '  File '
                                      '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                      'line 140, in try_catch\n'
                                      '    raise e\n'
                                      '  File '
                                      '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                      'line 137, in try_catch\n'
                                      '    result = func_result(*args, **kwargs)\n'
                                      '  File '
                                      '"D:\\git_ui\\sensecity_ui\\v\\scripts\\Main_flow\\main_user_role\\UserDep.py", '
                                      'line 31, in action\n'
                                      '    if not '
                                      'self.p_user.del_dep(dep_name=df_name_new):\n'
                                      '  File '
                                      '"D:\\git_ui\\sensecity_ui\\v\\pub\\pub_user_manage.py", '
                                      'line 142, in del_dep\n'
                                      '    self.driver.ele_click(el_lst[-1])\n'
                                      "TypeError: 'bool' object is not "
                                      'subscriptable\n',
                        'test_expect': '可以创建、查看、编辑和删除部门',
                        'test_log': 'User dep的日志',
                        'test_name': '部门管理',
                        'test_result': False,
                        'test_step': '页面左下方的“设置”，点击“用户管理”，右键一级部门出现“创建下级”、“查看详情”、“编辑”、“删除”按钮'},
            'UserSearch': {'script_author': 'csf',
                           'test_case': 'SC_user_003',
                           'test_error': None,
                           'test_expect': '可以根据关键字查询;可以根据条件筛选结果',
                           'test_log': 'UserSearch的日志',
                           'test_name': '查询、筛选用户',
                           'test_result': True,
                           'test_step': '页面右上角的搜索框中输入关键词（姓名），点击搜索按钮;通过导航栏关键词，根据部门、角色、状态筛选'}
        },

        "main_task_center": {
            'AAAA': {'script_author': 'csf',
                     'test_case': 'SC_user_001',
                     'test_error': 'Traceback (most recent call last):\n'
                                   '  File '
                                   '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                   'line 47, in run\n'
                                   '    self.try_catch("测试体", self.action)\n'
                                   '  File '
                                   '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                   'line 140, in try_catch\n'
                                   '    raise e\n'
                                   '  File '
                                   '"D:\\git_ui\\sensecity_ui\\common\\base_class.py", '
                                   'line 137, in try_catch\n'
                                   '    result = func_result(*args, **kwargs)\n'
                                   '  File '
                                   '"D:\\git_ui\\sensecity_ui\\v\\scripts\\Main_flow\\main_user_role\\UserDep.py", '
                                   'line 31, in action\n'
                                   '    if not '
                                   'self.p_user.del_dep(dep_name=df_name_new):\n'
                                   '  File '
                                   '"D:\\git_ui\\sensecity_ui\\v\\pub\\pub_user_manage.py", '
                                   'line 142, in del_dep\n'
                                   '    self.driver.ele_click(el_lst[-1])\n'
                                   "TypeError: 'bool' object is not "
                                   'subscriptable\n',
                     'test_expect': '可以创建、查看、编辑和删除部门',
                     'test_log': 'User dep的日志',
                     'test_name': '部门管理',
                     'test_result': False,
                     'test_step': '页面左下方的“设置”，点击“用户管理”，右键一级部门出现“创建下级”、“查看详情”、“编辑”、“删除”按钮'},
            'BBBB': {'script_author': 'csf',
                     'test_case': 'SC_user_003',
                     'test_error': None,
                     'test_expect': '可以根据关键字查询;可以根据条件筛选结果',
                     'test_log': 'UserSearch的日志',
                     'test_name': '查询、筛选用户',
                     'test_result': True,
                     'test_step': '页面右上角的搜索框中输入关键词（姓名），点击搜索按钮;通过导航栏关键词，根据部门、角色、状态筛选'}
        }
    }
    run_result = run_result or tst_data
    total_case = pass_case = fail_case = fail_retry_case = fail_retry_pass_case = error_case = 0
    html_content_table = []
    module_num = 1
    for k, sub_dict in run_result.items():
        sub_total = sub_pass = sub_fail = sub_error = 0
        html_content_table_sub = []
        module_case_num = 1
        for kk, v in sub_dict.items():
            if v['test_result']:
                sub_pass += 1
                tst_result = 'Pass'
                case_class = 'passCase'
            else:
                if v['test_error']:
                    sub_error += 1
                    tst_result = 'Error'
                    case_class = 'errorCase'
                else:
                    sub_fail += 1
                    tst_result = 'Fail'
                    case_class = 'failCase'
            if 'retry' in v['test_name']:
                fail_retry_case += 1
                sub_fail += 1
                if v['test_result']:
                    fail_retry_pass_case += 1
            sub_total += 1
            now_tr_sub = html_body_loop_sub.format(
                v['test_case'],
                v['test_name'],
                get_tst_log(v['test_log']),
                tst_result,
                case_class,
                v['test_error'] if v.get('test_error') else '空',
                'pt{}.{}'.format(module_num, module_case_num),
            )
            html_content_table_sub.append(now_tr_sub)
            module_case_num += 1
        if sub_pass and not sub_fail and not sub_error:
            case_set_class = 'passClass'
        else:
            case_set_class = 'failClass'
        pass_case += sub_pass
        fail_case += sub_fail
        error_case += sub_error
        total_case += sub_total
        now_tr = html_body_loop.format(
            case_set_class,
            k,
            sub_total,
            sub_pass,
            sub_fail,
            sub_error,
            module_num,
        )
        html_content_table.append(now_tr)
        html_content_table.extend(html_content_table_sub)
        module_num += 1
    html_content_all = ''.join(html_content_table)
    html_body_1_format = html_body_1.format(
        time_dict['start_time'],
        time_dict['end_time'],
        time_dict['cost_time'],
        pass_case,
    )
    html_body_count_format = html_body_count.format(pass_case, fail_case - fail_retry_pass_case, error_case, total_case)
    html_end_format = html_end % dict(
        Pass=str(pass_case - fail_retry_pass_case),
        fail_retry_pass=str(fail_retry_pass_case),
        # error=str(error_case),
        fail=str(fail_case - fail_retry_pass_case),
    )
    html_body_11_format = html_body_11.format(
        str(pass_case),
        str(fail_case),
        str(fail_retry_case),
        str(fail_retry_pass_case),
        str(error_case),
    )
    # print(run_result)
    html_all = html_head + html_body_1_format + html_body_11_format + html_content_all + html_body_count_format + html_end_format

    with open(report_name, 'w', encoding='utf-8') as f:
        f.write(html_all)
