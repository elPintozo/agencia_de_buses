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
        new_name_for_route: '',
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
                self.title = 'Assing bus | Route ID '+route_id
                self.bus_list = response.data
            })
        },
        get_assinged_buses: function (route_id){
            var self = this;
            self.show_btn_add = false
            self.show_checkbox = false
            self.show_btn_remove = false
            self.selected_route = route_id;

            axios.get('/garage/api/route/get_assinged_buses/'+route_id+'/').then(function (response){
                self.title = 'Assinged buses | Route ID '+route_id
                self.bus_list = response.data
            })
        },
        unassing_bus: function (route_id){
            var self = this;
            self.show_btn_add = false
            self.show_btn_remove = true
            self.show_checkbox = true
            self.selected_route = route_id;

            axios.get('/garage/api/route/unassing_bus/'+route_id+'/').then(function (response){
                self.title = 'Unassing bus | Route ID '+route_id
                self.bus_list = response.data
            })
        },
        add_bus: function (){
            var self = this;
            var data = {
                'route': self.selected_route,
                'buses_selected': self.selected_buses
            }
            axios.post('/garage/api/route/add/bus/', data).then(function (response){
                self.selected_buses = []
                self.get_assinged_buses(self.selected_route)
            })
            
        },
        remove_bus: function (){
            var self = this;
            var data = {
                'route': self.selected_route,
                'buses_selected': self.selected_buses
            }
            axios.post('/garage/api/route/remove/bus/', data).then(function (response){
                self.selected_buses = []
                self.get_assinged_buses(self.selected_route)
            })
        },
        btn_add_new_route: function (){
            var self = this;
            var data = {
                'name': self.new_name_for_route,
            }
            axios.post('/garage/api/route/list', data).then(function (response){
                self.new_name_for_route = ''
                self.get_route_list()
            })
        },

    },
    beforeMount(){
        this.get_route_list()
     },
});