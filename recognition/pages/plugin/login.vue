<template>
	<view class="login-containter">
		<image class="bg-img" src="/static/login.jpg"></image>
		<!-- <view class="title">
			欢迎登录果蔬识别系统!
		</view> -->
		
		<view class="avatar">
			<u-avatar  :src="src" shape="circle" size="100" class=""></u-avatar>
			
		</view>
		<view class="username">
			<view class="" v-if="islogin">
				{{username}}
			</view>
		</view>
		<!-- <view class="btn-login-bottom">
			<!-- <text class="tips-text" >登陆后识别次数更多哦</text> -->
			<!-- <u-notice-bar :text="text1" v-if="!islogin"></u-notice-bar>
			<u-notice-bar :text="text2" v-if="islogin"></u-notice-bar>
		</view> --> -->
		 
		<!-- <view class="login1" v-if="islogin">
			<view class="">
				个人中心
			</view>
		</view> -->
		
		<view class="btn-login-top">
			<button type="primary" class="btn-llogin" @click="getUserInfo()" v-if="!islogin">一键登录</button>
			
		</view>
		
		<view class="">
			<u-collapse
			    @change="change"
			    @close="close"
			    @open="open"
				v-if="islogin"
			  >
			    <u-collapse-item
				icon="man-add"
			      title="剩余次数"
			      name="Docs guide"
			    >
			      <text class="u-collapse-content">您的剩余次数还有10次</text>
			    </u-collapse-item>
			    <u-collapse-item
				icon="chat"
			      title="联系管理员"
			      name="Variety components"
			    >
			      <text class="u-collapse-content">联系管理员可以增加次数</text>
			    </u-collapse-item>
			    <u-collapse-item
				icon="edit-pen"
			      title="意见反馈"
			      name="Numerous tools"
			    >
			      <text class="u-collapse-content">如果使用小程序过程中产生了问题，可以向管理员反馈</text>
			    </u-collapse-item>
			  </u-collapse>
		</view>
		
		
		<view class="">
			<button v-if="islogin" @click="logOut()">退出</button>
		</view>
		<view class="">
			<button @tap="goRank">查看排行榜</button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				islogin:false,
				userInfo:{},
				src: '',
				text1:'登陆后识别次数更多哦',
				text2:'登陆成功！',
				username:''
			};
		},
		methods:{
			getUserInfo(){
				const that=this
				uni.getUserProfile({
					desc: 'weixin',
					success(e){
						console.log(e.userInfo)
						uni.setStorageSync('userInfo',e.userInfo)
						that.islogin=true
						that.userInfo=e.userInfo
						that.src=e.userInfo.avatarUrl
						that.username=e.userInfo.nickName
						
					},
					fail(){
						uni.showToast({
							icon:null,
							title:'您取消了登录授权'
						})
					}
				})
				
			},
			logOut(){
				uni.removeStorageSync('userInfo')
				this.islogin=false
				 this.src='',
				 this.username=''
			},
			goRank(){
				uni.navigateTo({
					url:"/pages/rankdetail/rankdetail"
				})
				
			}
			
		},
		mounted() {
			const userInfo = uni.getStorageSync('userInfo')
			console.log(userInfo)
			this.islogin=userInfo? true : false
			this.userInfo=userInfo
			
			// this.src=userInfo.avatarUrl
		}
	}
</script>

<style lang="scss">
	.title{
		margin-top: 30rpx;
		margin-left: 20rpx;
		font-size: 46rpx;
		color: #000000;
	}
	.bg-img{
			position: absolute;
		    z-index: -1;
		    left: 0;
		    right: 0;
		    bottom: 0;
		    right: 0;
		    width: 100%;
		    height: 100%;
	}
	.login-containter{
		
		.avatar{
			
			height: 200px;
			
			
			
			display: flex;
			align-items: center;
			justify-content: center;
		}
		.username{
			display: flex;
			align-items: center;
			justify-content: center;
			font-size: 30rpx;
			color: #6a6a6a;
		}
	
		.btn-login-top{
			display: flex;
			align-items: center;
			justify-content: center;
			margin-top: 40px;
			.btn-llogin{
				width: 50%;
				border-radius: 100px;
				margin: 15px 0;
				
				background-color: #06b1fa;
				justify-content: center;
			}
		}
		.btn-login-bottom{
			display: flex;
			align-items: center;
			justify-content: center;
		}
		
		.tips-text{
			font-size: 12px;
			color: gray;
			justify-content: center;
		}
		.login1{
			margin-top: 60px;
		}
		
	}
</style>
