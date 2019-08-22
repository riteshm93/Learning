import Vue from 'vue';
import FlowChart from './components/FlowChart.vue';

const app = new Vue({
    el:'#app',
    data:{
      listitems:[{name: 'Roy', power: 9000}, {name: 'Duke', power: 7000}],
      search: ''
    },
    components: {
      FlowChart
    },
    computed: {
      data: function (): Object[] {
        var search: string = this.search;
        var result: Object[] = [];
        this.listitems.forEach(function(item){
          if(item.name.search(search)!= -1){
            result.push(item);
          }
        });
        return result;
      }
    }
  })