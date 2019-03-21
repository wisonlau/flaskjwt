<template>
	<div id="login">
		<div class="l-right">
			<div class="l-l">
				 <!-- @tab-click="handleClick" -->
				<el-tabs v-model="activeName">
					<el-tab-pane label="用户登录" name="first">
						<!-- el-form:自定义表单组件 -->
					    <!-- :model="form" 表单对象，用于收集收据 -->
					    <!-- label-width="80px"：label的宽度 -->
					    <!-- el-form-item：表单项  -->
						<el-form ref="form" status-icon :rules="rules" :model="form" label-width="80px">
							<el-form-item  prop="username">
								<el-input v-model="form.username" placeholder="请输入用户名" prefix-icon="iconfont icon-yonghuming"></el-input>
							</el-form-item>
							<el-form-item  prop="password">
								<!-- 将来我们给组件注册事件的时候，可以会注册不上 -->
								<!--@keyup.enter点击键盘的enter触发事件-->
								<!-- .native: 注册事件，给组件的根元素注册事件 -->

								<el-input type="password" v-model="form.password" placeholder="请输入密码" @keyup.enter.native="login" prefix-icon="iconfont icon-mima"></el-input>
							</el-form-item>
							<el-form-item>
								<!--使用@语法糖绑定事件-->
								<el-button type="primary" @click="login">登录</el-button>
								<el-button @click="reset">重置</el-button>
							</el-form-item>
						</el-form>
					</el-tab-pane>
					<el-tab-pane label="帅哥登录" name="second">长得很帅</el-tab-pane>
				</el-tabs>
			</div>
			
		</div>
	</div>
</template>

<script>
	 export default {
		data () {
			return {
//				定义一些变量,可以使用{{}}语法在页面中直接获取
				activeName: 'first',
				form: {
					username: 'wison',
					password: "wison"
				},
				rules: {
					username: [
						{ required: true, message: '请输入用户名', trigger: 'change' },
						{ min: 3, max: 6, message: '长度在 3 到 6 个字符', trigger: 'change' }
					],
					password: [
						{ required: true, message: '请输入密码', trigger: 'change' },
						{ min: 3, max: 12, message: '长度在 3 到 12 个字符', trigger: 'change' }
					]
				}
			}
		},
		mounted() {
			this.checkLogin()
		},
		methods: {
			login () {
			 //  先触发页面中的检验规则,不通过给提示,通过就向后台发送请求,
          	 //  $refs是vue中获取页面的,在html中要写 ref="form"
		     this.$refs.form.validate(async (valid) => {
				 if (valid) {
					let data = new URLSearchParams()
					for (var key in this.form) {
						data.append(key, this.form[key])
35             		}
                    this.axios.post('http://192.168.173.132:8888/api/admin/login', data).then(response => {
                        if (response.status == 200 && response.data) {
							localStorage.setItem('myToken', 'JWT '+response.data.data.token); // 设置拦截，可以用cookie等，在控制台中的Application中查看
							localStorage.setItem('name', response.data.data.user.name);
							this.$message.success('恭喜你，登录成功') // 登录成功的提示
							this.$router.push('homeMain');
                        }
                    }).catch(function (error) {
                    	this.$message.error('登录失败');
                    });
				 }
			 })
			},
			reset () {
				this.$refs.form.resetFields()//清空输入框中的信息
				// 数据被我写死了,可以自行改动
			},
			checkLogin()
			{
				if(localStorage.getItem('myToken'))
				{
					this.axios.get('http://192.168.173.132:8888/api/admin/user', {headers:{ 'Authorization':localStorage.getItem('myToken')}}).then(response => {
						if (!response.data.error_code) {
							this.$router.push('homeMain');
						}
						else
						{
							localStorage.removeItem('myToken')
							localStorage.removeItem('name')
						}
					}).catch(function (error) {
						this.$message.error('登录失败');
					});
				}
				
			}
		}
  };
</script>
<!--使用less-->
<style lang="less">
	
	#login {
		width: 100%;
		height: 100%;
		.l-right {
			width: 100%;
			height: 100%;
			position: relative;
			.l-l {
				/*使用定位法居中元素,如果不考虑兼容性的问题可以使用flex布局居中代码简洁,简单粗暴*/
				/*定位法:子绝对定位,父级相对定位,如果相应的父级没有定位,会顺着html的结构往最顶的父级找*/
				width: 350px;
				height:350px;
				position:absolute;
				top:50%;
				left:50%;
				margin-top: -175px;
				margin-left: -175px;
				.el-tabs {
					width: 100%;
				}
				.el-form-item__content {
					margin-left: inherit !important;
				}
			}
		}
		#tab-first {
			width: 175px;
			text-align: center;
		}
		#tab-second {
		    text-align: center;
			width: 175px;
		}
	}
	/*使用媒体查询,这是在小于1400px的屏幕宽中的样式*/
	@media only screen and (max-width: 1400px){
		.l-l {
			width: 253px !important;
			height:350px;
			.el-tabs__item {
				padding: inherit !important;
				
			}
			
			 #tab-second {
				width: 125px !important;
			}
			
			 #tab-first {
				width: 125px !important;
			}
			}
	}
</style>
