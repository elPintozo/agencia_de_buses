new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        bus_list:[],
        new_plate_for_bus:'',      
    },
    methods:{
        get_bus_list: function (){
            var self = this;

            axios.get('/garage/api/bus/list').then(function (response){
                self.bus_list = response.data
            })
        },
        btn_add_new_bus: function (){
            var self = this;
            var data={
                'plate':self.new_plate_for_bus
            }
            axios.post('/garage/api/bus/list', data).then(function (response){
                self.new_plate_for_bus = ''
                self.get_bus_list()
            })
        }
    },
    beforeMount(){
        this.get_bus_list()
     },
});