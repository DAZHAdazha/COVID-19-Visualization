<template>
  <div>
    <div id="rose-chart">
      <div id="china-map"></div>
      <rose-circle class="roseCircle" :jwsr="jwsr"></rose-circle>
    </div>
    <div id="world-map"></div>
  </div>
</template>

<script>
import echarts from 'echarts'
import china from 'echarts/map/json/china.json'
import world from 'echarts/map/json/world.json'
import roseCircle from './roseCircle'
echarts.registerMap('china', china) // 注册对应的地图;
echarts.registerMap('world', world)

export default {
  name: 'RoseChart',
  components: {
    roseCircle
  },
  props: {
    china: Array,
    world: Array,
    jwsr: Array
  },
  data () {
    return {
      otherlist: [],
      chinaOption: {
        title: {
          text: '中国疫情今日新增分布图',
          top: 20,
          left: 20,
          textStyle: {
            color: 'white'
          }
        },
        tooltip: {
          triggerOn: 'click',
          formatter: function (e, t, n) {
            return e.value === 0.5
              ? e.name + '：有疑似病例'
              : e.seriesName + '<br />' + e.name + '：' + e.value
          }
        },
        visualMap: {
          min: 0,
          max: 250,
          left: 26,
          bottom: 28,
          textStyle: { color: '#eeeeee' },
          showLabel: false,
          text: ['高', '低'],
          inRange: {
            color: ['#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
          },
          show: !0
        },
        geo: {
          map: 'china',
          roam: !1,
          zoom: 0.8,
          scaleLimit: {
            min: 0.8,
            max: 2
          },
          // top: 20,
          label: {
            normal: {
              show: false,
              fontSize: '14',
              color: 'rgba(0,0,0,0.7)'
            },
            emphasis: {
              color: '#f46d43'
            }
          },
          itemStyle: {
            normal: {
              // shadowBlur: 50,
              // shadowColor: 'rgba(0, 0, 0, 0.2)',
              borderColor: 'rgba(0, 0, 0, 0.2)'
            },
            emphasis: {
              areaColor: '#F9F900',
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              borderWidth: 0
            }
          }
        },
        series: [
          {
            name: '确诊病例',
            type: 'map',
            geoIndex: 0,
            data: []
          }
        ]
      },

      worldOption: {
        title: {
          text: '世界累计感染者分布图',
          top: 20,
          left: 20,
          textStyle: {
            color: 'white'
          }
        },
        tooltip: {
          triggerOn: 'click',
          formatter: function (e, t, n) {
            return e.value === 0.5
              ? e.name + '：有疑似病例'
              : e.seriesName + '<br />' + e.name + '：' + e.value
          }
        },
        visualMap: {
          min: 0,
          max: 2500000,
          left: 26,
          bottom: 40,
          showLabel: true,
          text: ['高', '低'],
          textStyle: { color: '#eeeeee' },
          inRange: {
            color: ['#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
          },
          show: !0
        },
        nameMap: {
          Afghanistan: '阿富汗',
          Singapore: '新加坡',
          Angola: '安哥拉',
          Albania: '阿尔巴尼亚',
          'United Arab Emirates': '阿联酋',
          Argentina: '阿根廷',
          Armenia: '亚美尼亚',
          'French Southern and Antarctic Lands':
              '法属南半球和南极领地',
          Australia: '澳大利亚',
          Austria: '奥地利',
          Azerbaijan: '阿塞拜疆',
          Burundi: '布隆迪',
          Belgium: '比利时',
          Benin: '贝宁',
          'Burkina Faso': '布基纳法索',
          Bangladesh: '孟加拉国',
          Bulgaria: '保加利亚',
          'The Bahamas': '巴哈马',
          'Bosnia and Herzegovina': '波斯尼亚和黑塞哥维那',
          Belarus: '白俄罗斯',
          Belize: '伯利兹',
          Bermuda: '百慕大',
          Bolivia: '玻利维亚',
          Brazil: '巴西',
          Brunei: '文莱',
          Bhutan: '不丹',
          Botswana: '博茨瓦纳',
          'Central African Republic': '中非共和国',
          Canada: '加拿大',
          Switzerland: '瑞士',
          Chile: '智利',
          China: '中国',
          'Côte d\'Ivoire': '科特迪瓦',
          Cameroon: '喀麦隆',
          'Dem. Rep. Congo': '刚果（金）',
          Colombia: '哥伦比亚',
          'Costa Rica': '哥斯达黎加',
          Cuba: '古巴',
          'Northern Cyprus': '北塞浦路斯',
          Cyprus: '塞浦路斯',
          'Czech Republic': '捷克共和国',
          Germany: '德国',
          Djibouti: '吉布提',
          Denmark: '丹麦',
          'Dominican Republic': '多明尼加共和国',
          Algeria: '阿尔及利亚',
          Ecuador: '厄瓜多尔',
          Egypt: '埃及',
          Eritrea: '厄立特里亚',
          Spain: '西班牙',
          Estonia: '爱沙尼亚',
          Ethiopia: '埃塞俄比亚',
          Finland: '芬兰',
          Fiji: '斐济',
          'Falkland Islands': '福克兰群岛',
          France: '法国',
          Gabon: '加蓬',
          'United Kingdom': '英国',
          Georgia: '格鲁吉亚',
          Ghana: '加纳',
          Guinea: '几内亚',
          Gambia: '冈比亚',
          'Guinea Bissau': '几内亚比绍',
          Greece: '希腊',
          Greenland: '格陵兰',
          Guatemala: '危地马拉',
          'French Guiana': '法属圭亚那',
          Guyana: '圭亚那',
          Honduras: '洪都拉斯',
          Croatia: '克罗地亚',
          Haiti: '海地',
          Hungary: '匈牙利',
          Indonesia: '印度尼西亚',
          India: '印度',
          Ireland: '爱尔兰',
          Iran: '伊朗',
          Iraq: '伊拉克',
          Iceland: '冰岛',
          Israel: '以色列',
          Italy: '意大利',
          Jamaica: '牙买加',
          Jordan: '约旦',
          Japan: '日本',
          Kazakhstan: '哈萨克斯坦',
          Kenya: '肯尼亚',
          Kyrgyzstan: '吉尔吉斯斯坦',
          Cambodia: '柬埔寨',
          Kosovo: '科索沃',
          Kuwait: '科威特',
          Laos: '老挝',
          Lebanon: '黎巴嫩',
          Liberia: '利比里亚',
          Libya: '利比亚',
          'Sri Lanka': '斯里兰卡',
          Lesotho: '莱索托',
          Lithuania: '立陶宛',
          Luxembourg: '卢森堡',
          Latvia: '拉脱维亚',
          Morocco: '摩洛哥',
          Moldova: '摩尔多瓦',
          Madagascar: '马达加斯加',
          Mexico: '墨西哥',
          Macedonia: '马其顿',
          Mali: '马里',
          Myanmar: '缅甸',
          Montenegro: '黑山',
          Mongolia: '蒙古国',
          Mozambique: '莫桑比克',
          Mauritania: '毛里塔尼亚',
          Malawi: '马拉维',
          Malaysia: '马来西亚',
          Namibia: '纳米比亚',
          'New Caledonia': '新喀里多尼亚',
          Niger: '尼日尔',
          Nigeria: '尼日利亚',
          Nicaragua: '尼加拉瓜',
          Netherlands: '荷兰',
          Norway: '挪威',
          Nepal: '尼泊尔',
          'New Zealand': '新西兰',
          Oman: '阿曼',
          Pakistan: '巴基斯坦',
          Panama: '巴拿马',
          Peru: '秘鲁',
          Philippines: '菲律宾',
          'Papua New Guinea': '巴布亚新几内亚',
          Poland: '波兰',
          'Puerto Rico': '波多黎各',
          'Dem. Rep. Korea': '朝鲜',
          Portugal: '葡萄牙',
          Paraguay: '巴拉圭',
          Qatar: '卡塔尔',
          Romania: '罗马尼亚',
          Russia: '俄罗斯',
          Rwanda: '卢旺达',
          'Western Sahara': '西撒哈拉',
          'Saudi Arabia': '沙特阿拉伯',
          Sudan: '苏丹',
          'S. Sudan': '南苏丹',
          Senegal: '塞内加尔',
          'Solomon Islands': '所罗门群岛',
          'Sierra Leone': '塞拉利昂',
          'El Salvador': '萨尔瓦多',
          Somaliland: '索马里兰',
          Somalia: '索马里',
          'Republic of Serbia': '塞尔维亚',
          Suriname: '苏里南',
          Slovakia: '斯洛伐克',
          Slovenia: '斯洛文尼亚',
          Sweden: '瑞典',
          Swaziland: '斯威士兰',
          Syria: '叙利亚',
          Chad: '乍得',
          Togo: '多哥',
          Thailand: '泰国',
          Tajikistan: '塔吉克斯坦',
          Turkmenistan: '土库曼斯坦',
          'East Timor': '东帝汶',
          'Trinidad and Tobago': '特里尼达和多巴哥',
          Tunisia: '突尼斯',
          Turkey: '土耳其',
          'United Republic of Tanzania': '坦桑尼亚',
          Uganda: '乌干达',
          Ukraine: '乌克兰',
          Uruguay: '乌拉圭',
          'United States': '美国',
          Uzbekistan: '乌兹别克斯坦',
          Venezuela: '委内瑞拉',
          Vietnam: '越南',
          Vanuatu: '瓦努阿图',
          'West Bank': '西岸',
          Yemen: '也门',
          'South Africa': '南非',
          Zambia: '赞比亚',
          Korea: '韩国',
          Tanzania: '坦桑尼亚',
          Zimbabwe: '津巴布韦',
          Congo: '刚果（布）',
          'Central African Rep.': '中非共和国',
          Serbia: '塞尔维亚',
          'Bosnia and Herz.': '波黑',
          'Czech Rep.': '捷克',
          'W. Sahara': '西撒哈拉',
          'Lao PDR': '老挝',
          'Dem.Rep.Korea': '朝鲜',
          'Falkland Is.': '福克兰群岛',
          'Timor-Leste': '东帝汶',
          'Solomon Is.': '所罗门群岛',
          Palestine: '巴勒斯坦',
          'N. Cyprus': '北塞浦路斯',
          Aland: '奥兰群岛',
          'Fr. S. Antarctic Lands': '法属南半球和南极陆地',
          Mauritius: '毛里求斯',
          Comoros: '科摩罗',
          'Eq. Guinea': '赤道几内亚',
          'Guinea-Bissau': '几内亚比绍',
          'Dominican Rep.': '多米尼加',
          'Saint Lucia': '圣卢西亚',
          Dominica: '多米尼克',
          'Antigua and Barb.': '安提瓜和巴布达',
          'U.S. Virgin Is.': '美国原始岛屿',
          Montserrat: '蒙塞拉特',
          Grenada: '格林纳达',
          Barbados: '巴巴多斯',
          Samoa: '萨摩亚',
          Bahamas: '巴哈马',
          'Cayman Is.': '开曼群岛',
          'Faeroe Is.': '法罗群岛',
          'IsIe of Man': '马恩岛',
          Malta: '马耳他共和国',
          Jersey: '泽西',
          'Cape Verde': '佛得角共和国',
          'Turks and Caicos Is.': '特克斯和凯科斯群岛',
          'St. Vin. and Gren.': '圣文森特和格林纳丁斯'
        },
        geo: {
          map: 'world',
          roam: !1,
          scaleLimit: {
            min: 1,
            max: 2
          },
          zoom: 1.22,
          label: {
            normal: {
              show: false,
              fontSize: '14',
              color: 'rgba(0,0,0,0.7)'
            },
            emphasis: {
              color: '#f46d43'
            }
          },
          itemStyle: {
            normal: {
              // shadowBlur: 50,
              // shadowColor: 'rgba(0, 0, 0, 0.2)',
              borderColor: 'rgba(0, 0, 0, 0.2)'
            },
            emphasis: {
              areaColor: '#F9F900',
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              borderWidth: 0
            }
          }
        },
        series: [
          {
            name: '确诊病例',
            type: 'map',
            geoIndex: 0,
            data: []
          }
        ]
      }
    }
  },
  watch: {
    china (newData, oldData) {
      this.china = newData
      this.china.forEach(element => {
        this.chinaOption.series[0].data.push({name: element.name, value: parseInt(element.econNum)})
      })
      var chinaMap = echarts.init(document.getElementById('china-map'))
      let tempOptionChina = JSON.parse(JSON.stringify(this.chinaOption))
      chinaMap.setOption(tempOptionChina)
    },

    world (newData, oldData) {
      this.world = newData
      this.world.forEach(element => {
        this.worldOption.series[0].data.push({name: element.name, value: parseInt(element.value)})
      })

      var worldMap = echarts.init(document.getElementById('world-map'))

      let tempOptionWorld = JSON.parse(JSON.stringify(this.worldOption))
      worldMap.setOption(tempOptionWorld)
    }
  }
}
</script>

<style lang="less">

  #rose-chart{
    height: 220px;
    display: flex;
    flex-direction: row;
    justify-content: space-between
  }

  #china-map{
    width: 60%;
    height: 300px;
  }

  .roseCircle{
    width: 40%;
    height: 220px;
  }

  #world-map{
    width: 100%;
    height: 400px;
    position: relative;
    top: 50px
  }

  .rose-chart-title {
    height: 50px;
    font-weight: bold;
    text-indent: 20px;
    font-size: 20px;
    display: flex;
    align-items: center;
  }

  .dv-charts-container {
    height: calc(~"100% - 50px");
  }
// }
</style>
