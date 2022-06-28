<template>
	<view class="common-page">
		<!-- <image class="logo" src="/static/logo.png"></image> -->
		<view class="title">
			今日推荐水果
		</view>
		<u-scroll-list @right="right" @left="left">
			<view class="scroll-list" style="flex-direction: row;">
				<view class="scroll-list__goods-item" v-for="(item, index) in list" :key="index"
					:class="[(index === 9) && 'scroll-list__goods-item--no-margin-right']">
					<image class="scroll-list__goods-item__image" :src="item.thumb"></image>
					<text class="scroll-list__goods-item__text">{{ item.price }}</text>
				</view>
				<view class="scroll-list__show-more">
					<text class="scroll-list__show-more__text">查看更多</text>
					<u-icon name="arrow-leftward" color="#f56c6c" size="12"></u-icon>
				</view>
			</view>
		</u-scroll-list>
		<view class="title">
			今日推荐蔬菜
		</view>
		<view>
			<u-grid :border="true" col="3">
				<u-grid-item v-for="(listItem,listIndex) in list1" :key="listIndex">
					<u-icon :customStyle="{paddingTop:20+'rpx'}" :name="listItem.name" :size="22"></u-icon>
					<text class="grid-text">{{listItem.title}}</text>
				</u-grid-item>
			</u-grid>
			<u-toast ref="uToast" />
		</view>
		<view class="showImg">
			<!-- <image v-if="imageSrc==''"  src="/static/show_img.png" mode=""></image> -->
			<image v-if="imageSrc!==''" :src="imageSrc" mode="" mode=""></image>
		</view>
		<view class="title">
			识别蔬菜水果
		</view>
		<!-- <view v-if="result==''" class="show_name">橙子</view>
		<view v-if="result!==''" class="show_name">{{result}}</view> -->
		<u-popup :show="show" mode="bottom" @close="close" @open="open" :round="20">
			<view class="container1">

				<image src="/static/相机.png" mode="" @click="clickMe('camera')" class="left"></image>
				<image src="/static/上传.png" mode="" @click="clickMe('album')" class="right"></image>
				<!-- <button @click="clickMe('album')">相册</button>
				
					
				        <button @click="clickMe('camera')">拍照</button>
				<!-- <view class="text1">点我拍照</view>
				<view class="text2">点我上传</view> -->
			</view>

		</u-popup>
		<view class="contain_camera_img">
			<image class="camera_img" src="/static/camera1.jpeg" @click="show = true"></image>
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
				announce: '',
				result: '',
				list: [{
					price: '樱桃',
					thumb: 'https://cdn.uviewui.com/uview/goods/1.jpg'
				}, {
					price: '菠萝',
					thumb: 'https://cdn.uviewui.com/uview/goods/2.jpg'
				}, {
					price: '西瓜',
					thumb: 'https://cdn.uviewui.com/uview/goods/6.jpg'
				}, {
					price: '苹果',
					thumb: 'https://cdn.uviewui.com/uview/goods/5.jpg'
				}, {
					price: '草莓',
					thumb: 'https://cdn.uviewui.com/uview/goods/2.jpg'
				}, {
					price: '荔枝',
					thumb: 'https://cdn.uviewui.com/uview/goods/3.jpg'
				}, {
					price: '梨',
					thumb: 'https://cdn.uviewui.com/uview/goods/4.jpg'
				}, {
					price: '桃子',
					thumb: 'https://cdn.uviewui.com/uview/goods/1.jpg'
				}],
				list1: [{
						name: 'photo',
						title: '白菜'
					},
					{
						name: 'lock',
						title: '黄瓜'
					},
					{
						name: 'star',
						title: '西红柿'
					},
					{
						name: 'hourglass',
						title: '油麦菜'
					},
					{
						name: 'home',
						title: '茄子'
					},
					{
						name: 'star',
						title: '红薯'
					},
				],
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
									$that.result = data.result
									console.log(data.result);
								} else {
									$that.result = data.msg
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
			clickMe2() {
				const $that = this
				uni.request({
					url: 'https://www.rainlotus.cc:5000/caigou',
					method: "POST",
					data: {
						name: "王元",
						age: "18"
					},
					success(res) {
						console.log(res.data);
						$that.announce = res.data.result
					}
				})
			},
			open() {
				// console.log('open');
			},
			close() {
				this.show = false
				// console.log('close');
			},
			left() {
				console.log('left');
			},
			right() {
				console.log('right');
			},
			click(name) {
				this.$refs.uToast.success(`点击了第${name}个`)
			},
			
		}
	}
</script>

<style lang="scss">
	.scroll-list {
		@include flex(column);

		&__goods-item {
			margin-right: 20px;

			&__image {
				width: 60px;
				height: 60px;
				border-radius: 4px;
			}

			&__text {
				color: #f56c6c;
				text-align: center;
				font-size: 12px;
				margin-top: 5px;
			}
		}

		&__show-more {
			background-color: #fff0f0;
			border-radius: 3px;
			padding: 3px 6px;
			@include flex(column);
			align-items: center;

			&__text {
				font-size: 12px;
				width: 12px;
				color: #f56c6c;
				line-height: 16px;
			}
		}
	}

	.grid-text {
	        font-size: 14px;
	        color: #909399;
	        padding: 10rpx 0 20rpx 0rpx;
	        /* #ifndef APP-PLUS */
	        box-sizing: border-box;
	        /* #endif */
			}
	.title {
		font-size: 46rpx;
		font-weight: 600;
		margin-bottom: 40rpx;
		padding-left: 40rpx;
	}


	.content {
		display: flex;
		align-items: center;
		justify-content: center;

	}

	.showImg {
		display: flex;
		align-items: center;
		justify-content: center;
	}

	

	.text-area {
		display: flex;
		justify-content: center;
	}

	.title {
		font-size: 36rpx;
		color: #8f8f94;
	}

	.container {
		display: flex;
	}

	.text1 {
		position: absolute;
		bottom: 80upx;
		left: 100upx;
		font-size: 20px;
	}

	.text2 {
		position: absolute;
		bottom: 80upx;
		right: 100upx;
		font-size: 20px;
	}

	.contain_camera_img {
		display: flex;
		align-items: center;
		justify-content: center;

	}

	.camera_img {
		height: 200px;
		weight: 800px;
	}

	.show_name {
		font-size: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.container1 {
		display: flex;
		justify-content: space-around;
		align-items: center;
		height: 100px;
	}

	.left {
		height: 80px;
		width: 80px;

	}

	.right {
		height: 80px;
		width: 80px;
	}
</style>
