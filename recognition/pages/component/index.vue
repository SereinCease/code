<template>
	<view class="common-page">
		<!-- <image class="logo" src="/static/logo.png"></image> -->
		<view class="showImg">
			<image v-if="imageSrc==''"  src="/static/show_img.png" mode=""></image>
			<image v-if="imageSrc!==''" :src="imageSrc" mode="" mode=""></image>
		</view>
		
		<view v-if="result==''" class="show_name">橙子</view>
		<view v-if="result!==''" class="show_name">{{result}}</view>
		<u-popup :show="show"  mode="bottom"  @close="close" @open="open" :round="20">
			<view class="container1">
				
				<image src="/static/照相机.png" mode="" @click="clickMe('camera')" class="left"></image>
				<image src="/static/图片.png" mode="" @click="clickMe('album')" class="right"></image>	
				        <!-- <button @click="clickMe('album')">相册</button>
				
					
				        <button @click="clickMe('camera')">拍照</button>
				<!-- <view class="text1">点我拍照</view>
				<view class="text2">点我上传</view> -->
			</view>
			
		</u-popup>
		<view class="contain_camera_img">
			<image class="camera_img" src="/static/recognition.jpg" @click="show = true"></image>
		</view>
		
		
		
		
		<!-- <button @click="clickMe2">点我2</button> -->
		<!-- <image v-if="imageSrc!==''" :src="imageSrc" mode=""></image> -->
		<div v-if="announce!==''">{{announce}}</div>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				show: false,
				imageSrc: '',
				announce:'',
				result:''
			}
		},
		onLoad() {

		},
		methods: {
			clickMe(val) {
				const $that = this
				uni.chooseImage({
					count: 1,
					sizeType: ['original', 'compressed'],
					sourceType: [val],
					success(res) {
						// tempFilePath可以作为img标签的src属性显示图片
						const tempFiles = res.tempFilePaths[0]
						$that.imageSrc = ''
						console.log(res);
						uni.uploadFile({
							url: 'https://www.rainlotus.cc:5000/upload', //仅为示例，非真实的接口地址
							filePath: tempFiles, //res.tempFilepaths
							header: {
								"Content-Type": "multipart/form-data"
							},
							name: 'file', // 文件对应的key ，默认 为 file
							// formData: {
							//   'user': 'test'
							// }, //上传额外携带的参数
							success(res) {
								const data = JSON.parse(res.data)
								console.log(data);
								if (data.code === '200') {
									$that.imageSrc = data.url
									$that.result =  data.result
									console.log(data.result);
								} else {
									$that.result =  data.msg
									console.log(data.msg)
								}
							},
							fail: () => {
								uni.showToast("图片上传失败，请联系开发！")
							},
						})
					}
				})
			},
			clickMe2(){
				const $that = this
				uni.request({
					url:'https://www.rainlotus.cc:5000/caigou',
					method:"POST",
					data:{
						name:"王元",
						age:"18"
					},
					success(res){
						console.log(res.data);
						$that.announce=res.data.result
					}
				})
			},
			open() {
			        // console.log('open');
			      },
			      close() {
			        this.show = false
			        // console.log('close');
			      }
		}
	}
</script>

<style>
	
	.content {
		display: flex;
		align-items: center;
		justify-content: center;
		
	}
	.showImg{
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.logo {
		height: 200rpx;
		width: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx;
	}

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}
	.container{
		display: flex;
	}
	.text1{
		position: absolute;
		bottom:80upx;
		left:100upx;
		font-size: 20px;
	}
	.text2{
		position: absolute;
		bottom:80upx;
		right:100upx;
		font-size: 20px;
	}
	.contain_camera_img{
		display: flex;
		align-items: center;
		justify-content: center;
		
	}
	.camera_img{
		height: 200px;
		weight:800px;
	}
	.show_name{
		font-size: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
	}
	.container1{
		display: flex;
		          justify-content: space-between;
		          align-items:center;
				  height: 100px;
	}
	.left{
		height: 80px;
		
	}
	.right{
		height: 100px;
		
	}
	
	
</style>
