new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        selected_route:'',
        selected_buses:[],
        route_list:[],
        bus_list:[],
        title:'',
        show_btn_add: false,
        show_btn_remove: false,
        show_checkbox:false,
    },
    methods:{
        get_route_list: function (){
            var self = this;

            axios.get('/garage/api/route/list').then(function (response){
                self.route_list = response.data
            })
        },
        assing_bus: function (route_id){
            var self = this;
            self.show_btn_add = true
            self.show_checkbox = true
            self.show_btn_remove = false
            self.selected_route = route_id;

            axios.get('/garage/api/route/assing_bus/'+route_id+'/').then(function (response){
                self.title = 'Assing bus'
                self.bus_list = response.data
                console.log(response.data)
            })
        },
        get_assinged_buses: function (route_id){
            var self = this;
            self.show_btn_add = false
            self.show_checkbox = false
            self.show_btn_remove = false
            self.selected_route = route_id;

            axios.get('/garage/api/route/get_assinged_buses/'+route_id+'/').then(function (response){
                self.title = 'Assinged buses'
                self.bus_list = response.data
                console.log(response.data)
            })
        },
        unassing_bus: function (route_id){
            var self = this;
            self.show_btn_add = false
            self.show_btn_remove = true
            self.show_checkbox = true
            self.selected_route = route_id;

            axios.get('/garage/api/route/unassing_bus/'+route_id+'/').then(function (response){
                self.title = 'Unassing bus'
                self.bus_list = response.data
                console.log(response.data)
            })
        },
        add_bus: function (){
            var self = this;
            var data = {
                'route': self.selected_route,
                'buses_selected': self.selected_buses
            }
            axios.post('/garage/api/route/add/bus/', data).then(function (response){
                console.log(response.data)
                self.selected_buses = []
            })
            
        },
        remove_bus: function (){
            var self = this;
            var data = {
                'route': self.selected_route,
                'buses_selected': self.selected_buses
            }
            axios.post('/garage/api/route/remove/bus/', data).then(function (response){
                console.log(response.data)
                self.selected_buses = []
            })
        }

    },
    beforeMount(){
        this.get_route_list()
     },
});