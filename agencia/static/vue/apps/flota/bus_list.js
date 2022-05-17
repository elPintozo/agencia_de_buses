new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        bus_list:[]      
    },
    methods:{
        get_bus_list: function (){
            var self = this;

            axios.get('/garage/api/bus/list').then(function (response){
                self.bus_list = response.data
            })
        }
    },
    beforeMount(){
        this.get_bus_list()
     },
});