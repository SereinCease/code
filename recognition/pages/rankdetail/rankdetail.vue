<template>
	<view class="container">
			<view class="body">
				<view class="ranking_list">
					<scroll-view scroll-x="true" class="ranking_state_tab" scroll-with-animation>
						<block v-for="(item,index) in rankingList" :key="index">
							<view @click="rankingTabs(index)">
								<text :class="rankingStatus == index ? 'rankingStatus' : '' ">{{item.title}}</text>
							</view>
						</block>
					</scroll-view>
					<swiper style="height: 100%;" :duration="500" @change="rankingChange" :current="rankingCurrent">
						<swiper-item v-for="(item,index) in rankingList" :key="index">
							<view class="table">
								<view class="th">
									<block v-for="(itemM,indexM) in item.menu" :key="indexM">
										<text>{{itemM}}</text>
									</block>
								</view>
								<block v-for="(itemD,indexD) in item.data" :key="indexD">
									<view class="td">
										<text v-if="itemD.key==1" class="num num1">{{itemD.key}}</text>
										<text v-else-if="itemD.key==2" class="num num2">{{itemD.key}}</text>
										<text v-else-if="itemD.key==3" class="num num3">{{itemD.key}}</text>
										<text v-else class="num">{{itemD.key}}</text>
										<text>{{itemD.name}}</text>
										<text>{{itemD.num}}</text>
										<text>{{itemD.username}}</text>
									</view>
								</block>
								<view class="more">查看更多</view>
							</view>
						</swiper-item>
					</swiper>
				</view>
			</view>
		</view>
	
	
</template>

<script>
	export default {
		data() {
			return {
				rankingList: [{
									title: '水果识别排行',
									menu: ["排名", "名称", "识别次数","用户名称"],
									data: [{key: 1, name: "草莓", num: "15",username:"一夜枝头白"},
										{key: 2, name: "樱桃", num: "15",username:"一夜枝头白"},
										{key: 3, name: "葡萄", num: "15",username:"一夜枝头白"},
										{key: 4, name: "香蕉", num: "15",username:"一夜枝头白"},
										{key: 5, name: "菠萝", num: "15",username:"一夜枝头白"}]
								}, {
									title: '蔬菜识别排行',
									menu: ["排名", "名称", "识别次数","用户名称"],
									data: [{key: 1, name: "白菜", num: "15",username:"一夜枝头白"},
										{key: 2, name: "菠菜", num: "15",username:"一夜枝头白"},
										{key: 3, name: "大葱", num: "15",username:"一夜枝头白"},
										{key: 4, name: "黄瓜", num: "15",username:"一夜枝头白"},
										{key: 5, name: "大头菜", num: "15",username:"一夜枝头白"}]
								}],
								rankingStatus: 0, //标记本月排行选中
								rankingCurrent: 0, //标记本月排行切换
				
				
			};
		},
		methods: {
					//点击排行切换swiper
					rankingTabs(index) {
						this.rankingStatus = index;
						this.rankingCurrent = index;
					},
					//滑动切换swiper
					rankingChange(e) {
						let index = e.detail.current;
						this.rankingStatus = index;
						this.rankingCurrent = index;
					},
				}
		
	}
</script>

<style lang="scss">
	view,
		scroll-view,
		swiper,
		swiper-item {
			box-sizing: border-box;
		}
	 
		page {
			background-color: #F8F8F8;
		}
	 
		.container {
			width: 100%;
			height: 100%;
			box-sizing: border-box;
			padding: 0;
			margin: 0;
		}
	 
		.body {
			padding: 30rpx;
	 
			.ranking_list {
				width: 100%;
				height: 712rpx;
				background: #FFFFFF;
				border-radius: 20rpx;
				overflow: hidden;
	 
				.ranking_state_tab {
					width: 100%;
					height: 82rpx;
					line-height: 82rpx;
					white-space: nowrap;
					overflow: hidden;
					box-sizing: border-box;
					display: inline-block;
					font-size: 24rpx;
					font-family: PingFang SC;
					font-weight: 400;
					color: #333333;
	 
					view {
						width: calc(100% / 2);
						height: 82rpx;
						display: inline-block;
						white-space: nowrap;
						text-align: center;
						position: relative;
	 
						text {
							width: 222rpx;
						}
					}
	 
					.rankingStatus {
						font-size: 28rpx;
						font-weight: 500;
					}
	 
					.rankingStatus:after {
						content: "";
						display: block;
						height: 6rpx;
						width: 55rpx;
						background: #265DDD;
						position: absolute;
						left: calc(50% - 27.5rpx); // 55/2=27.5 是宽度的一半
						bottom: 0;
						border-radius: 12rpx;
					}
				}
	 
				.table {
					background: #FDFFFF;
	 
					.th {
						border-radius: 20rpx 20rpx 0rpx 0rpx;
						height: 80rpx;
						background: #F4F6FF;
						font-size: 20rpx;
						font-family: PingFang SC;
						font-weight: bold;
						color: #333333;
						display: flex;
						align-items: center;
						padding: 0 30rpx;
	 
						text {
							width: calc(85% / 3);
							text-align: center;
						}
	 
						& text:first-child {
							width: 15%;
						}
					}
	 
					.td {
						height: 90rpx;
						font-size: 24rpx;
						font-family: DIN;
						font-weight: 500;
						color: #333333;
						display: flex;
						align-items: center;
						white-space: nowrap;
						margin: 0 30rpx;
						border-bottom: 1px solid #eee;
						border-width: thin;
	 
						text {
							width: calc(85% / 3);
							text-align: center;
							white-space: nowrap;
							overflow: hidden;
							text-overflow: ellipsis;
						}
	 
						& text:first-child {
							width: 15%;
						}
	 
						.num {
							font-size: 32rpx;
							font-weight: bold;
							color: #333333;
						}
	 
						.num1 {
							color: #F12C03;
						}
	 
						.num2 {
							color: #F8780D;
						}
	 
						.num3 {
							color: #2B87FF;
						}
					}
	 
					.more {
						height: 90rpx;
						display: flex;
						flex-direction: column;
						align-items: center;
						justify-content: center;
						text-align: center;
						font-size: 24rpx;
						font-family: PingFang SC;
						font-weight: 500;
						color: #999999;
					}
				}
	 
			}
		}
	
</style>
