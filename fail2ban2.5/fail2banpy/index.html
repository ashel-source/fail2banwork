<style>
        #fromSiteConfig input,
        #fromServerConfig input{
            width: 300px;
        }
        .actStyle{
            margin:0px;
            display: block;
            padding-top: 6px;
        }
        .log_box{
            background-color: #fafafa;
            border: #ddd 1px solid;
            padding: 0;
            float: left;
            margin-bottom: 15px;
            width: 100%;
        }
        .log_box .line{
            width: 25%;
            text-align: center;
            height: 70px;
            float: left;
            margin: 6px 0;
        }
        .log_box .line .name{
            width: auto;
            display: block;
            text-align: center;
            margin: 5px 0 8px;
            color: #666;
        }
        .log_box .line .val{
            font-size: 18px;
            display: block;
            text-align: center;
            font-weight: bold;
        }
        .log_style th{font-weight:normal}
    </style>
    <div class="bt-form" id="plugin">
        <div class="bt-w-main">
            <div class="bt-w-menu">
                <p class="bgw">站点保护</p>
                <p>服务保护</p>
                <p>IP黑名单</p>
                <p>IP白名单</p>
                <p>服务状态</p>
<!--                <p>自定义防护</p>-->
            </div>
            <div class="bt-w-con pd15 divtable">
                <div class="bt-box active">
                    <div class="mb10">
                        <button class="btn btn-success btn-sm" onclick="Fail2ban.set_site_config('addNew')" style="margin-top: -3px;">创建</button>
                        <div class="divtable mtb15">
                            <table class="table table-hover">
                            <thead>
                                <tr><th>保护模式</th>
                                    <th>状态</th>
                                    <th>最大重试次数</th>
                                    <th>端口</th>
                                    <th>周期</th>
                                    <th>禁止时间</th>
                                    <th style="text-align: right;">操作</th>
                                </tr>
                            </thead>
                            <tbody id="anti_siteTable"></tbody>
                            </table>
                        </div>
                    </div>
                    <ul class="help-info-text c7" style="margin-top:30px">
                        <li>通过日志可查看封锁数据、解除被封IP。</li>
                        <li><font style="color:red">站点功能目前仅支持Nginx，apache和更多功能敬请期待。</font></li>
                    </ul>
                </div>
                <div class="bt-box" style="display: none;">
                    <div class="mb10">
                        <button class="btn btn-success btn-sm" onclick="Fail2ban.set_server_config('addNew')" style="margin-top: -3px;">创建</button>
                        <div class="divtable mtb15">
                            <table class="table table-hover">
                            <thead>
                                <tr><th>保护服务</th>
                                    <th>状态</th>
                                    <th>最大重试次数</th>
                                    <th>端口</th>
                                    <th>周期</th>
                                    <th>禁止时间</th>
                                    <th style="text-align: right;">操作</th>
                                </tr>
                            </thead>
                            <tbody id="anti_serverTable"></tbody>
                            </table>
                        </div>
                    </div>
                    <ul class="help-info-text c7" style="margin-top:30px">
                        <li>用于保护某个服务，每个模式只可创建一次。</li>
                        <li>通过日志可查看封锁数据、解除被封IP。</li>
                    </ul>
                </div>
                <div class="bt-box" style="display: none;">
                    <textarea name="black_ip" id="blackIP" cols="40" rows="15" placeholder="192.168.1.0/24" style="padding: 2px"></textarea>
                    <button class="btn btn-success btn-sm" onclick="Fail2ban.set_blackIP_config()" style="margin-top: 20px;display: block;">保存</button>
                    <ul class="help-info-text c7" style="margin-top:30px">
                        <li>如有多个请以换行隔开</br>例：192.168.1.1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;192.168.1.0/24</li>
                    </ul>
                </div>
                <div class="bt-box" style="display: none;">
                    <textarea name="white_ip" id="whileIP" cols="40" rows="15" style="padding: 2px"></textarea>
                    <button class="btn btn-success btn-sm" onclick="Fail2ban.set_whiteIP_config()" style="margin-top: 20px;display: block;">保存</button>
                    <ul class="help-info-text c7" style="margin-top:30px">
                        <li>添加白名单的IP将跳过封锁条件，如有多个请以换行隔开</br>例：192.168.1.1</br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;192.168.1.0/24</li>
                    </ul>
                </div>
                <div class="bt-box" style="display: none;">
                    <div class="mb10 startBox"></div>
                </div>
								<div class="bt-box" style="display: none;">
                    <div id="custom-protection" class="mb10"></div>
										<ul class="help-info-text c7" style="margin-top:30px">
                    </ul>
                </div>
            </div>
        </div>
    </div>
    <script type="text/html" id="site_anti_config">
        <form class="bt-form pd20 pb70" id="fromSiteConfig">
            <div class="line">
                <span class="tname">状态</span>
                <div class="info-r c4">
                    <span class="btswitch-p actStyle"><input class="btswitch btswitch-ios" id="fail_checkbox" type="checkbox">
                    <label class="btswitch-btn fail_label" for="fail_checkbox"></label>
                    </span>
                </div>
            </div>
            <div class="line">
                <span class="tname">最大重试次数</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_max" placeholder="最大重试次数：80 单位次"/> &nbsp;次
                </div>
            </div>
            <div class="line">
                <span class="tname">周期</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_find" placeholder="周期：300 单位秒"/> &nbsp;秒
                </div>
            </div>
            <div class="line">
                <span class="tname">禁止时间</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_ban" placeholder="禁止时间：600 单位秒" style="vertical-align: middle;"/> 
                    <span style="display: inline-block; color:#ccc; margin-left:10px; font-size:12px; vertical-align: middle;">
                        注意：默认（秒），或者带上单位s/m/h/d
                    </span>
                </div>
            </div>
            <div class="line">
                <span class="tname">端口</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_port" placeholder="监听的端口：80,443"/>
                </div>
            </div>
            <div class="line">
                <span class="tname">保护模式</span>
                <div class="info-r c4">
                    <select class="bt-input-text site_select_mode" ></select>
                </div>
            </div>
            <div class="line">
                <span class="tname">站点</span>
                <div class="info-r c4">
                    <select class="bt-input-text site_select_value" ></select>
                </div>
            </div>
            <div class="line" style="display: none">
                <span class="tname">目录/文件</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_dir" placeholder="输入目录/文件 : /dir 或 /dir/index.html"/>
                </div>
            </div>
            <ul class="help-info-text c7">
                <li>简单防CC：检查到站点日志文件在设置周期内(300秒)有超过最大重试次数(30次)的IP访问，将禁止该IP访问600秒(默认禁止时间)</li>
                <li>防站点扫描：检查到站点日志文件在设置周期内(300秒)有超过最大重试次数(30次)的IP访问保护的目录或文件，将禁止该IP访问600秒(默认禁止时间)</li>
           </ul>
        </form>
    </script>
    <script type="text/html" id="server_anti_config">
        <form class="bt-form pd20 pb70" id="fromServerConfig">
            <div class="line">
                <span class="tname">状态</span>
                <div class="info-r c4">
                    <span class="btswitch-p actStyle"><input class="btswitch btswitch-ios" id="fail_server_checkbox" type="checkbox">
                    <label class="btswitch-btn fail_server_label" for="fail_server_checkbox"></label>
                    </span>
                </div>
            </div>
            <div class="line">
                <span class="tname">最大重试次数</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="server_max" placeholder="最大重试次数: 80 单位次"/> &nbsp;次
                </div>
            </div>
            <div class="line">
                <span class="tname">周期</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="server_find" placeholder="周期：300 单位秒"/> &nbsp;秒
                </div>
            </div>
            <div class="line">
                <span class="tname">禁止时间</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="site_ban" placeholder="禁止时间：600 单位秒" style="vertical-align: middle;"/> 
                    <span style="display: inline-block; color:#ccc; margin-left:10px; font-size:12px; vertical-align: middle;">
                        注意：默认（秒），或者带上单位s/m/h/d
                    </span>
                </div>
            </div>
            <div class="line">
                <span class="tname">端口</span>
                <div class="info-r c4">
                    <input class="bt-input-text" type="text" name="server_port" placeholder="端口： 22"/>
                </div>
            </div>
            <div class="line">
                <span class="tname">保护服务</span>
                <div class="info-r c4">
                    <select class="bt-input-text server_select_mode" ></select>
                </div>
            </div>
            <!--<ul class="help-info-text c7">-->
                <!--<li>状态：开启/关闭防爆破</li>-->
                <!--<li>最大重试次数：失败最大容忍次数</li>-->
                <!--<li>周期：周期内超过最大容忍次数将会禁止该ip</li>-->
                <!--<li>禁止时间：禁止时间。</li>-->
                <!--<li>端口：禁止的ip将无法访问以下端口，多个请用逗号隔开(传递空值将禁止访问所有) 例：80,443</li>-->
                <!--<li>保护服务：防爆破的模式</li>-->
            <!--</ul>-->
            <ul class="help-info-text c7">
                <li>监控保护的服务日志，在设置周期内(300秒)有超过最大重试次数(30次)的IP访问，将禁止该IP访问600秒(默认禁止时间)</li>
                <li>mysql默认情况下可能不会输出登录日志导致无法检查，如果无法触发请手动设置日志等级</li>
            </ul>
        </form>
    </script>
    <script type="text/html" id="site_log_dialog">
        <div class="pd15 log_style">
            <div class="log_box"></div>
            <div class="table-box" style="float: left;width: 100%;margin-bottom: 20px;">
                <div class="tbThead">
                    <table class="table table-hover">
                        <thead>
                            <tr><th>IP</th><th style="text-align: right;">操作</th></tr>
                        </thead>
                    </table>
                </div>
                <div class="tbTbody" style="max-height: 180px;overflow: auto;margin-top: -21px;">
                    <table class="table table-hover">
                        <tbody id="site_banned_Table"></tbody>
                    </table>
                </div>
            </div>
            <!--<ul class="help-info-text c7">-->
                <!--<li>Currently Failed: 当前连接失败次数。</li>-->
                <!--<li>Total Banned: 封锁的IP总数。</li>-->
                <!--<li>Total Failed：连接失败总数。</li>-->
                <!--<li>Currently Banned：当前封锁IP数</li>-->
            <!--</ul>-->
        </div>
    </script>
    <script>
        var Fail2ban = {
            serviceStatus: false,
            site_list: [],
            mode_list: {
                site: [],
                server: []
            },
            zh_mode_list: {
            	0: '简单防CC',
            	1: '防止站点扫描'
            },
            plugin_name: 'fail2ban',
            init: function(){
                var _this = this;
                _this.get_status_verify();
                _this.get_site_anti();
                $('.layui-layer-page').width(900);
                $(".bt-w-menu p").click(function(){
                    var index = $(this).index();
                    $(this).addClass("bgw").siblings().removeClass("bgw");
                    $('.bt-w-con .bt-box').eq(index).show().siblings().hide();
                    switch(index){
                        case 0:
                            if(!serviceStatus){
                                layer.msg("Please start the Fail2ban service first!",{icon:2});
                                return;
                            }
                            _this.get_site_anti();
                            break;
                        case 1:
                            if(!serviceStatus){
                                layer.msg("Please start the Fail2ban service first!",{icon:2});
                                return;
                            }
                            _this.get_server_anti();
                            break;
                        case 3:
                            _this.get_whiteIP(function(res){
                                $('textarea[name=white_ip]').val(res)
                            });
                            break;
                        case 2:
                            //_this.get_blackIP();
                            _this.black_IP(function(res){
                                $('textarea[name=black_ip]').val(res)
                            });
                            break;
                        case 4:
                            _this.get_status_verify();
                            break;
												case 5:
														if(!serviceStatus){
																layer.msg("Please start the Fail2ban service first!",{icon:2});
																return;
														}
														_this.get_custom_protection();
														break;		
                    }
                });
                // 点击开关
                $('#plugin').on('click','.ServiceAdmin',function(){
                    var index = $(this).attr('data-index');
                    _this.SetService(index);
                });
                // 获取网站/服务器模式
                _this.get_mode_list(function(res){
                    _this.mode_list.site = res.site
                    _this.mode_list.server = res.server
                });
                // 获取站点
                _this.get_all_sitename(function(res){
                    for(item in res){
                        _this.site_list.push(item)
                    }
                })
            },
						// 自定义防护
						get_custom_protection: function(){
								var _this = this;
								// 使用公共方法 bt_tools.table 渲染表格
								bt_tools.table({
										el: '#custom-protection',
										url: '/plugin?action=a&name=fail2ban&s=get_anti_info',
										// data: data,
										dataFilter: function(res){
												return {
													data: res.custom
												}
										},
										title: '自定义防护列表',
										height: '380',
										default: '暂无数据',
										column: [
												{ fid: 'mode', title: '保护名称' },
												{
														fid: 'act',
														title: '状态',
														type: 'status',
														config: {
																icon: true,
																list: [
																		['true', '', 'bt_success', 'glyphicon-play'],
																		['false', '', 'bt_danger', 'glyphicon-pause']
																]
														}
												},
												{ fid: 'maxretry', title: '最大重试次数' },
												{ fid: 'port', title: '端口' },
												{ fid: 'findtime', title: '周期' },
												{ fid: 'bantime', title: '禁止时间' },
												{
														title: '操作',
														type: 'group',
														align: 'right',
														group: [
																{
																		title: '修改',
																		event: function (row, index, ev, key, that) {
																			_this.add_custom_protection(row, that);
																		}
																},
																{
																		title: '日志',
																		event: function (row, index, ev, key, that) {
																				// 使用已有的日志打开方法
																				Fail2ban.open_log_view(row.mode, row.act);
																		}
																},
																{
																		title: '删除',
																		event: function (row, index, ev, key, that) {
																			Fail2ban.del_anti_config(row.mode, that);
																		}
																}
														]
												}
										],
										tootls: [
												{
														type: 'group',
														positon: ['left', 'top'],
														list: [{
																title: '创建',
																active: true,
																event: function (ev, that) {
																	_this.add_custom_protection(null, that);
																}
														}]
												}
										],
								});
						},
						// 添加/编辑自定义防护
						add_custom_protection: function(row, that){
								var _this = this;
								var addForm = bt_tools.open({
										title: row ? '修改自定义防护' : '创建自定义防护',
										area: '540px',
										content: {
												class: 'pd20',
												data: row ? {
													...row,
													mode: row.mode.replace('custom-','')} : {
													maxretry: 5,
													findtime: 60,
													bantime: 600,
													port: '80,443',
												},
												form: [
														{
																label: '保护名称',
																group:  [
																	{
																		type: 'other',
																		boxcontent: '<div class="flex align-center mr5" style="height: 32px;">custom-</div>',
																	},
																	{ 
																	type: 'text', 
																	name: 'mode', 
																	width: '250px', 
																	placeholder: '请输入保护名称' 
																}
																]
														},
														{
																label: '日志路径',
																group: { 
																	type: 'text', 
																	name: 'logpath', 
																	width: '300px', 
																	placeholder: '请选择日志路径',
																	icon: {
																		type: 'glyphicon-folder-open',
																		select: 'file',//非必填，可限制选择目录或文件[dir|file]
																		defaultPath:'', //非必填，每次打开后的路径
																		event: function (formData, element, that, ev) {
																				// 点击图标时触发
																		},
																		callback: function (path) {
																				// 选中后回调
																			// if (path) {
																			// 	_this.getLastLog(addForm, path);
																			// }
																		},
																},
																}
														},
														{
															label: '详细日志',
															class: 'desc-log',
															group: [
																{
																// type: 'select',
																type: 'text',
																name: 'log_content',
																width: '300px',
																disabled: true,
																placeholder: '请选择日志路径后选择详细日志',
																// list: []
															},{
																type: 'button',
																active: false,
																name: 'submitForm',
																title: '选择日志',
																event: function (formData, element, _that) {
																	_this.select_log_file(formData.logpath, _that)
																}
															},
															]
														},
														// {
														// 		label: '状态',
														// 		group: {
														// 			type: 'other',
														// 			boxcontent:
														// 				'<div class="flex align-center" style="height: 32px;">\
														// 															<input class="btswitch btswitch-ios" id="act" name="act" type="checkbox" ' +
														// 				(row?.act === 'true' || !row ? 'checked' : '') +
														// 				'>\
														// 															<label class="btswitch-btn" for="act" style="margin: 0;"></label>\
														// 													</div>',
														// 		},
														// },
														{
																label: '端口',
																group: { type: 'text', name: 'port', width: '300px', placeholder: '监听端口：80,443' }
														},
														{
																label: '屏蔽关键词',
																group: { type: 'text', name: 'keyword', width: '300px', placeholder: '例如: 404' }
														},
														{
																label: '日志格式',
																group: [
																	{
																		type: 'other',
																		boxcontent: '<div class="flex align-center mr5" style="height: 32px;">IP地址在关键词</div>',
																	},
																	{
																		type: 'select',
																		name: 'keyword_position',
																		width: '150px',
																		placeholder: '未知',
																		list: [
																			{ title: '前面', value: 'after' },
																			{ title: '后面', value: 'before' },
																		],
																	}
																]

														},
													{
														label: ' ',
														group: {
															type: 'other',
															boxcontent: '<div  class="more-config btlink flex align-center mr5" style="height: 32px;"><span>点击查看，更多配置</span><span class="ml5 glyphicon glyphicon-chevron-down"></span></div>'
														}
													},
													{
															label: '最大重试次数',
															display: false,
															group: { 
																type: 'number', 
																name: 'maxretry', 
																width: '150px', 
																unit: '次',
															placeholder: '最大重试次数：80 单位次' 
														}
													},
													{
															label: '周期',
															display: false,
															group: { 
																type: 'number',
																	name: 'findtime', 
																	width: '150px', 
																	unit: '秒',
																	placeholder: '周期：300 单位秒'}
													},
													{
															label: '禁止时间',
															display: false,
															group: { type: 'number', name: 'bantime', width: '150px', unit: '秒', placeholder: '禁止时间：600 单位秒'}
													},
													{
														group: {
															type: 'help',
															list: [
																'<span style="color: red;">封禁触发条件：在60秒内，若同一IP在80/443端口应用服务日志中出现5次匹配关键词，自动封禁该IP 600秒</span>',
																'<span style="color: red;">日志格式：日志格式设置：请定义日志中 IP 地址与关键词的相对位置。设置完成后，系统将实时拦截并封禁违规IP</span>'
															]
														}
													}
												]
										},
										success: function(layero){
											$(layero).find('.layui-layer-content').css('overflow','inherit');
											// 更多配置展开
											$(layero).find('.more-config').click(function(){
												var isShow = $(this).find('span:eq(1)').hasClass('glyphicon-chevron-up');
												$(this).find('span:eq(0)').html(isShow ? '点击查看，更多配置' : '点击收起，更多配置');
												$(this).find('span:eq(1)').toggleClass('glyphicon-chevron-down').toggleClass('glyphicon-chevron-up');
												addForm.form.config.form[7].display = !isShow;
												addForm.form.config.form[8].display = !isShow;
												addForm.form.config.form[9].display = !isShow;
												addForm.form.$replace_render_content(7);
												addForm.form.$replace_render_content(8);
												addForm.form.$replace_render_content(9);
											})
										},
										yes: function(formData, indexs){
												var obj = {
														type: row ? 'edit' : 'add',
														act: true,
														maxretry: parseInt(formData.maxretry) || 30,
														findtime: parseInt(formData.findtime) || 300,
														bantime: parseInt(formData.bantime) || 600,
														port: formData.port || '',
														mode: formData.mode.includes('custom-') ? formData.mode : 'custom-' + formData.mode,
														logpath: formData.logpath || '',
														keyword: formData.keyword || '',
														keyword_position: formData.keyword_position || 'before',
														log_id: addForm.form.config.data.log_id || ''
												};
												_this.set_anti(obj, function(res){
														if(res.status) {
															layer.close(indexs);
															that.$refresh_table_list()
														}
														layer.msg(res.msg, {icon: res.status?1:2});
												}, '正在'+ (row? '编辑': '创建') +'自定义防护，请稍后...');
										}
								});
							setTimeout(function(){
								$('.desc-log .bt_select_updown .bt_select_list').css({
									'width': 'max-content',
									'min-width': '100%',
									'max-width': '500px',
								})
							}, 150);
							if (row && addForm) {
								_this.getLastLog(addForm, row.logpath);
							}	
						},
						// 选择日志 弹窗 表格
						select_log_file: function(path, that){
							if (!path) {
								return layer.msg('请先选择日志路径', { icon: 2 });
							}
							var _this = this;
							var logTable = null;
							bt_tools.open({
								title: '选择日志文件',
								area: ['700px', '584px'],
								content: '<div class="pd20" id="select-log-box"></div>',
								success: function (layero, indexs) {
									// 使用公共方法 bt_tools.table 渲染表格
									logTable = bt_tools.table({
										el: '#select-log-box',
										url: '/plugin?action=a&name=fail2ban&s=get_last_log',
										param: { log_path: path },
										dataFilter: function(res){
											return {
												data: res
											}
										},
										title: '日志文件列表',
										height: '400',
										default: '暂无数据',
										column: [
											{
													type: 'checkbox',
													width: 20
											},
											{ fid: 'log_content',class: 'set_click',  title: '日志内容' },
										],
										tootls: [
											 {
													// 搜索内容
													type: 'search',
													positon: ['right', 'top'],
													placeholder: '请输入内容',
													searchParam: 'search', //搜索请求字段，默认为 search
													value: '', // 当前内容,默认为空
											},
										],
										success: function () {
											// 隐藏全选框
											$(layero).find('.bt_table thead tr th').eq(0).find('label').hide();
											// 处理单选框 只能选择一个
											$(layero).find('.bt_table tbody').off('click').on('click', '.cust—checkbox', function () {
												var index = $(this).parents('tr').index();
												$(this).parents('tr').siblings().find('.cust—checkbox-input').prop('checked', false);
												$(this).parents('tr').siblings().find('.cust—checkbox').removeClass('active');
												logTable.checkbox_list = [index]
											});
											$(layero).find('.set_click').parent().off('click').on('click', function(){
												$(this).prev().find('.cust—checkbox').click();
											})
										}
									});
								},
								yes: function (indexs) {
									console.log(logTable)
									if (logTable.checkbox_list.length == 0) {
										return layer.msg('请选择日志记录', { icon: 2 });
									}
									var currentLog = logTable.data[logTable.checkbox_list[0]];
									console.log(that)
									that.config.form[2].group[0].value = currentLog.log_content;
									that.config.data.log_id = currentLog.log_id;
									that.$replace_render_content(2);
									layer.close(indexs);
								}
							});
						},
						// 获取日志列表
						getLastLog: function(addForm, path){
							bt_tools.send({
								url: '/plugin?action=a&name=fail2ban&s=get_last_log',
								data: { log_path: path },
							}, function (res) {
								addForm.form.config.form[9].group.list = res.map(function (item) {
									return { title: item.log_content, value: item.log_id };
								});
								addForm.form.$replace_render_content(9)
							})							
						},
            // 获取开关状态
            get_status_verify: function(){
                this.get_fail2ban_status(function(res){
                    serviceStatus = res;
                    var sBody = '<div class="soft-man-con"><p class="status">状态: <span>'+(res?lan.public.on:lan.public.close)+'</span><span style="color: '+(res?'#20a53a':'red')+'; margin-left: 3px;" class="glyphicon glyphicon '+(res?'glyphicon-play':'glyphicon-pause')+'"></span></p>\
                    <div class="sfm-opt">\
                        <button class="btn btn-default btn-sm ServiceAdmin" data-index="'+( res?'stop':'start' )+'">'+(res?"停止":"启动")+'</button>\
                        <button class="btn btn-default btn-sm ServiceAdmin" data-index="restart" style="display:'+(res?'inline':'none')+';">重启</button>\
                        <button class="btn btn-default btn-sm ServiceAdmin" data-index="reload">重载</button>\
                    </div></div>'
                    $(".startBox").html(sBody);
                });
            },
            // 设置服务开关
            SetService:function(status){
                var _this = this;
                this.set_fail2ban_status({type:status},function(res){
                    if(res.status) _this.get_status_verify();
                })
            },
            // site 防爆破
            get_site_anti:function(){
                var _this = this;
                this.get_anti_info(function(rdata){
                    var tableBody = "",res = rdata.site;
                    if(JSON.stringify(rdata) == "{}"){
                        tableBody = '<tr><td colspan="7" style="text-align: center;">No data</td></tr>'
                    }else{
                        for(var i = 0; i<res.length; i++){
                            tableBody += '<tr><td>'+ res[i].mode +'</td>\
                                <td><span class="glyphicon '+(res[i].act == 'true'?'glyphicon-play':'glyphicon-pause')+'" style="color:'+(res[i].act == 'true'?'#20a53a':'red')+';font-size:12px"></span></td>\
                                <td>'+ res[i].maxretry +'</td>\
                                <td>'+ res[i].port +'</td>\
                                <td>'+ res[i].findtime +'</td>\
                                <td>'+ res[i].bantime +'</td>\
                                <td style="text-align: right;">\
                                    <a class="btlink" href="JavaScript:void(0)" onclick="Fail2ban.set_site_config(\'edit\',\''+res[i].mode +'\',\''+res[i].act +'\',\''+res[i].maxretry +'\',\''+res[i].port +'\',\''+res[i].findtime +'\',\''+res[i].bantime +'\',\''+res[i].dir +'\')">'+lan.public.edit+'</a>\
                                    &nbsp;&nbsp;|&nbsp;&nbsp;<a class="btlink" href="JavaScript:void(0)" onclick="Fail2ban.open_log_view(\''+res[i].mode+'\',\''+res[i].act+'\')">日志</a>\
                                    &nbsp;&nbsp;|&nbsp;&nbsp;<a class="btlink" style="color:red" href="JavaScript:void(0)" onclick="Fail2ban.del_anti_config(\''+res[i].mode+'\')">删除</a>\
                                </td></tr>'
                        }
                    }
                    $("#anti_siteTable").html(tableBody);
                });
            },
            // 获取封锁列表
            get_banned_log:function(val){
                var lineObj = '',tbody= '';
                this.get_status({mode:val},function(res){
                    if(res.status){
                        var _data = res.msg
                        lineObj = '<div class="line"><span class="name">封锁的IP总数</span><span class="val">'+_data.total_banned+'</span></div>\
                        <div class="line"><span class="name">连接失败总数</span><span class="val">'+_data.total_failed+'</span></div>\
                        <div class="line"><span class="name">当前封锁IP数</span><span class="val">'+_data.currently_banned+'</span></div>\
                        <div class="line"><span class="name">当前连接失败次数</span><span class="val">'+_data.currently_failed+'</span></div>'
                        $('.log_box').html(lineObj);

                        for(var i =0; i<_data.banned_ip_list.length; i++){
                            tbody += '<tr>\
                                <td>'+_data.banned_ip_list[i]+'</td>\
                                <td style="text-align: right;"><a style="color:red" href="JavaScript:void(0)" onclick="Fail2ban.del_site_banned_ip(\''+_data.banned_ip_list[i]+'\',\''+val+'\')">删除</a></td>\
                                </tr>'
                        }
                        $('#site_banned_Table').html(tbody);
                    }else{
                        layer.msg(res.msg,{icon:2})
                    }
                })
            },
            // 查看封锁日志
            open_log_view:function(site,status){
                var _this = this;
                if(status == 'false'){return layer.msg('保护已关闭',{icon:3})}
                layer.open({
                    type: 1,
                    area: '500px',
                    title: '禁止日志',
                    closeBtn: 2,
                    shift: 0,
                    content: site_log_dialog.innerHTML,
                    success:function (){
                        _this.get_banned_log(site);
                    }
                })
            },
            // 创建、修改网站配置
            set_site_config:function(type,mode,act,max,port,find,ban,dir){
                var _this = this,siteOpt='',modeOpt='',dirStatus = false;
                if (mode == undefined) {act = true,max = '30',port = '80,443',find = '300',ban = '600';}
                layer.open({
                    type: 1,
                    area: '500px',
                    title: type == 'addNew'? "创建": "修改",
                    closeBtn: 2,
                    shift: 0,
                    btn:['确认','取消'],
                    content: site_anti_config.innerHTML,
                    success: function(index){
                        if(type == 'addNew') {
                            for(var i = 0; i<_this.mode_list.site.length; i++){
                                modeOpt += '<option value="'+_this.mode_list.site[i]+'">'+_this.zh_mode_list[i]+'</option>'
                            }
                            for(var i = 0; i<_this.site_list.length; i++){
                                siteOpt += '<option value="'+_this.site_list[i]+'">'+_this.site_list[i]+'</option>'
                            }
                            $(".site_select_mode").html(modeOpt).css('width','300px');
                            $(".site_select_value").html(siteOpt).css('width','300px');
                            // 选择网站模式时
                            $('.site_select_mode').change(function(){
                                switch($('.site_select_mode').val()){
                                    case 'site-scan':
                                        dirStatus = true;
                                        $('#fromSiteConfig >.line:gt(6)').css('display','block');
                                    break;
                                    case 'site-cc':
                                        dirStatus = false;
                                        $('#fromSiteConfig >.line:eq(7)').css('display','none');
                                    break;
                                }
                            })
                            $("#fail_checkbox").prop("checked",act)
                        }else{
                            var val = mode.match(/-\w+/);
                            if(val == '-scan'){
                                dirStatus = true;
                                $('#fromSiteConfig >.line:eq(7)').css('display','block');
                                $('input[name=site_dir]').val(dir);
                            }
                            $('#fromSiteConfig >.line:eq(6)').css('display','none');
                            $(".site_select_mode").html('<option value="'+mode+'">'+mode+'</option>').attr('disabled',true).css({'background-color':'#f1f1f1','width':'300px'});
                            $("#fail_checkbox").prop("checked",act == 'true'?true: false)
                        }
                        $("input[name='site_max']").val(max);
                        $("input[name='site_find']").val(find);
                        $("input[name='site_ban']").val(ban);
                        $("input[name='site_port']").val(port);
                    }
                    ,yes: function(index){
                        var modeVal = $(".site_select_mode").val(),siteVal = $(".site_select_value").val(),temp='';
                        if(type == 'addNew'){
                            temp = siteVal + modeVal.match(/-\w+/)
                        }else{
                            temp = modeVal
                        }
                        var obj = {
                            type: type == 'addNew'? 'add': 'edit',
                            act: $("#fail_checkbox").prop("checked"),
                            maxretry: $("input[name='site_max']").val(),
                            findtime: $("input[name='site_find']").val(),
                            bantime: $("input[name='site_ban']").val(),
                            port: $("input[name='site_port']").val(),
                            mode: temp
                        }
                        if(dirStatus){obj['dir'] = $("input[name='site_dir']").val()}
                        _this.set_anti(obj,function(res){
                            if(res.status) layer.close(index);
                            layer.msg(res.msg,{icon:res.status?1:2})
                            _this.get_site_anti();
                        })

                    }
                });
            },
            // server 防爆破
            get_server_anti:function(){
                var _this = this;
                this.get_anti_info(function(rdata){
                    var tableBody = "",res = rdata.server;
                    if(JSON.stringify(rdata) == "{}"){
                        tableBody = '<tr><td colspan="7" style="text-align: center;">No data</td></tr>'
                    }else{
                        for(var i = 0; i<res.length; i++){
                            tableBody += '<tr><td>'+ res[i].mode +'</td>\
                                <td><span class="glyphicon '+(res[i].act == 'true'?'glyphicon-play':'glyphicon-pause')+'" style="color:'+(res[i].act == 'true'?'#20a53a':'red')+';font-size:12px"></span></td>\
                                <td>'+ res[i].maxretry +'</td>\
                                <td>'+ res[i].port +'</td>\
                                <td>'+ res[i].findtime +'</td>\
                                <td>'+ res[i].bantime +'</td>\
                                <td style="text-align: right;">\
                                    <a class="btlink" href="JavaScript:void(0)" onclick="Fail2ban.set_server_config(\'edit\',\''+res[i].mode +'\',\''+res[i].act +'\',\''+res[i].maxretry +'\',\''+res[i].port +'\',\''+res[i].findtime +'\',\''+res[i].bantime +'\')">'+lan.public.edit+'</a>\
                                    &nbsp;&nbsp;|&nbsp;&nbsp;<a class="btlink" href="JavaScript:void(0)" onclick="Fail2ban.open_log_view(\''+res[i].mode+'\',\''+res[i].act+'\')">日志</a>\
                                    &nbsp;&nbsp;|&nbsp;&nbsp;<a class="btlink" style="color:red" href="JavaScript:void(0)" onclick="Fail2ban.del_anti_config(\''+res[i].mode+'\')">删除</a>\
                                    </td></tr>'
                        }
                    }
                    $("#anti_serverTable").html(tableBody);
                });
            },
            // 黑名单
            get_blackIP:function(){
                var _this = this;
                this.get_black_ip(function(rdata){
                    var tableBody = "",res = rdata;
                    if(JSON.stringify(rdata) == "[]"){
                        tableBody = '<tr><td colspan="7" style="text-align: center;">空</td></tr>'
                    }else{
                        for(var i = 0; i<res.length; i++){
                            tableBody += '<tr><td>'+ res[i] +'</td>\
                                <td style="text-align: right;">\
                                    <a class="btlink" style="color:red" href="JavaScript:void(0)" onclick="Fail2ban.del_blackIP(\''+res[i]+'\')">删除</a>\
                                    </td></tr>'
                        }
                    }
                    $("#black_ip").html(tableBody);
                });
            },
            del_blackIP:function(ip){
                var _this = this,
                loadT=layer.confirm('确定要删除 ['+ip+'] 吗?',{icon:3, title: 'Delete blacklist IP'},function(){
                    layer.close(loadT);
                    _this.del_black_ip(ip);
                });
            },
            // 创建、修改服务器配置
            set_server_config:function(type,mode,act,max,port,find,ban){
                var _this = this,modeOpt='';
                if (mode == undefined) {act = true,max = '30',port = '',find = '300',ban = '600';}
                layer.open({
                    type: 1,
                    area: '500px',
                    title: type == 'addNew'? "创建": "修改",
                    closeBtn: 2,
                    shift: 0,
                    btn:['确认','取消'],
                    content: server_anti_config.innerHTML,
                    success: function(index){
                        if(type == 'addNew') {
                            for(var i = 0; i<_this.mode_list.server.length; i++){
                                modeOpt += '<option value="'+_this.mode_list.server[i]+'">'+_this.mode_list.server[i]+'</option>'
                            }
                            $(".server_select_mode").html(modeOpt).css('width','300px');

                            $("#fail_server_checkbox").prop("checked",act)
                        }else{
                            $(".server_select_mode").html('<option value="'+mode+'">'+mode+'</option>').attr('disabled',true).css({'background-color':'#f1f1f1','width':'300px'});
                            $("#fail_server_checkbox").prop("checked",act == 'true'? true : false)
                        }
                        $("input[name='server_max']").val(max);
                        $("input[name='server_find']").val(find);
                        $("input[name='server_ban']").val(ban);
                        $("input[name='server_port']").val(port);
                    }
                    ,yes: function(index){
                        var obj = {
                            type: type == 'addNew'? 'add': 'edit',
                            act: $("#fail_server_checkbox").prop("checked"),
                            maxretry: $("input[name='server_max']").val(),
                            findtime: $("input[name='server_find']").val(),
                            bantime: $("input[name='server_ban']").val(),
                            port: $("input[name='server_port']").val(),
                            mode: $(".server_select_mode").val()
                        }
                        _this.set_anti(obj,function(res){
                            _this.get_server_anti();
                            if(res.status) layer.close(index);
                            layer.msg(res.msg,{icon:res.status?1:2})
                        })
                    }
                });
            },
            // 删除防爆破配置
            del_anti_config:function(val, that){
                var _this = this;
                layer.confirm('真的要删除 ['+val+' ] 吗?',{icon:3, title: '删除防爆破设置'},function(){
                    _this.del_anti({mode:val},function(res){
                        layer.msg(res.msg,{icon:res.status?1:2,time:1000},function(){
													if (that) {
														that.$refresh_table_list()
													}else {
 														_this.get_site_anti();
                            _this.get_server_anti();
													}
                        })
                    })
                })
            },
            // 设置黑名单
            // set_blackIP_config:function(){
            // 	var _this = this;
            //     var ip = $('input[name=black_ip]').val();
            //     _this.set_black_ip({ip:ip},function(res){
            //     	_this.get_blackIP();
            //         layer.msg(res.msg,{icon:res.status?1:2});
            //     })
            // },
            set_blackIP_config:function(){
                var ip = $('textarea[name=black_ip]').val();
                this.set_black_ip({black_ip:ip},function(res){
                    layer.msg(res.msg,{icon:res.status?1:2})
                })
            },
            // 设置白名单
            set_whiteIP_config:function(){
                var ip = $('textarea[name=white_ip]').val();
                this.set_white_ip({white_ip:ip},function(res){
                    layer.msg(res.msg,{icon:res.status?1:2})
                })
            },
            // 解除ip封锁
            del_site_banned_ip:function(ip,site){
                var _this = this;
                layer.confirm('真的要删除 ['+ip+' ] 吗?', {icon: 3, title:'解除ip封锁',
                        closeBtn:2,
                        btn: ['确认','取消']
                },function(index,layers){
                    _this.ban_ip_release({ip:ip,mode:site},function(res){
                        layer.close(index);
                        layer.msg(res.msg,{icon:res.status?1:2});
                        _this.get_banned_log(site)
                    })
                }, function(index,lyaers){
                    layer.close(index);
                });
            },
            get_fail2ban_status:function(callback){
                this.send({
                    tips: "正在获取状态...",
                    method: 'get_fail2ban_status',
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            set_fail2ban_status:function(obj,callback){
                this.send({
                    tips: "正在设置状态...",
                    method: 'set_fail2ban_status',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            get_anti_info:function(callback){
                this.send({
                    tips: "获取Fail2ban 列表...",
                    method: 'get_anti_info',
                    success: function(res){
                        if(callback) callback(res);
                    }
                });
            },
            get_black_ip:function(callback){
                this.send({
                    tips: "正在获取黑名单列表...",
                    method: 'get_black_list',
                    success: function(res){
                        if(callback) callback(res);
                    }
                });
            },
            set_black_ip:function(obj,callback){
                this.send({
                    tips: '正在添加黑名单...',
                    method: 'ban_ip',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            del_black_ip:function(obj,callback){
            	var _this = this;
                _this.send({
                    tips: '正在删除黑名单...',
                    method: 'unban_ip',
                    data:{ip:obj},
                    success: function(res){
                    	_this.get_blackIP();
                    	layer.msg(res.msg,{icon:res.status?1:2});
                        if(callback) callback(res);
                    }
                })
            },
            get_status:function(obj,callback){
                this.send({
                    tips: '获取封锁数据中，请稍后...',
                    method: 'get_status',
                    data: obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            get_mode_list:function(callback){
                this.send({
                    tips: '正在获取模式中，请稍后...',
                    method: 'get_mode_list',
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            get_all_sitename:function(callback){
                this.send({
                    tips: '正在获取站点中，请稍后...',
                    method: 'get_all_sitename',
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            set_anti:function(obj,callback, tips){
                this.send({
                    tips: tips || '正在生成防爆破设置，请稍后...',
                    method: 'set_anti',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            del_anti:function(obj,callback){
                this.send({
                    tips: '正在删除防爆破设置中，请稍后...',
                    method: 'del_anti',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            set_white_ip:function(obj,callback){
                this.send({
                    tips: '正在设置白名单中，请稍后...',
                    method: 'set_white_ip',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            get_whiteIP:function(callback){
                this.send({
                    tips: '获取白名单中，请稍后...',
                    method: 'get_white_ip',
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            black_IP:function(callback){
                this.send({
                    tips: '获取黑名单中，请稍后...',
                    method: 'get_black_list',
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            ban_ip_release:function(obj,callback){
                this.send({
                    tips: '正在设置白名单中，请稍后...',
                    method: 'ban_ip_release',
                    data:obj,
                    success: function(res){
                        if(callback) callback(res);
                    }
                })
            },
            
            // 请求方法
            send:function(obj){
                var loadT = '';
                if (obj.load == undefined) obj.load = 0;
                if (obj.url == undefined) {
                    if (obj.plugin_name === undefined && this.plugin_name !== undefined) obj.plugin_name = this.plugin_name
                    if (!obj.plugin_name || !obj.method) {
                        layer.msg('The plugin class name, or plugin method name is missing!', {icon: 2 });
                        return false;
                    }
                }
                if (obj.load === 0 || obj.tips != '') {
                    loadT = layer.msg(obj.tips, {
                        icon: 16,
                        time: 0,
                        shade: 0.3
                    });
                } else if (obj.load === 1 || (obj.tips == undefined && obj.load == undefined)) {
                    loadT = layer.load();
                }
                $.ajax({
                    type: 'POST',
                    url: obj.url != undefined ? obj.url : ('/plugin?action=a&name=' + obj.plugin_name + '&s=' + obj.method),
                    data: obj.data || {},
                    timeout: obj.timeout || 99999999,
                    complete: function (res) {
                        if (obj.load === 0 || obj.load === 1) layer.close(loadT);
                    },
                    success: function (rdata) {
                        if (obj.check) {
                            obj.success(rdata);
                            return false
                        }
                        if (rdata.status === false) {
                            layer.msg(rdata.msg, { icon: 2 });
                            return false;
                        }
                        obj.success(rdata);
                    },
                    error: function (ex) {
                        if (!obj.error) {
                            obj.msg || obj.msg == undefined ? layer.msg('The request process found an error!', {
                                icon: 2
                            }) : '';
                            return;
                        }
                        return obj.error(ex);
                    }
                });
            }
        }
        Fail2ban.init();
    </script>
