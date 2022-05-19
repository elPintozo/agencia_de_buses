new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        selected_schedule:'',
        selected_route:[],
        route_list:[],
        schedule_list:[],
        title:'',
        show_btn_add: false,
        show_btn_remove: false,
        show_checkbox:false,          
    },
    methods:{
        get_schedule_list: function (){
            var self = this;

            axios.get('/garage/api/schedule/list').then(function (response){
                self.schedule_list = response.data
            })
        },
        assing_route: function (schedule_id){
            var self = this;
            self.show_btn_add = true
            self.show_checkbox = true
            self.show_btn_remove = false
            self.selected_schedule = schedule_id;
    
            axios.get('/garage/api/schedule/assing_route/'+schedule_id+'/').then(function (response){
                self.title = 'Assing route | Schedule ID '+schedule_id
                self.route_list = response.data
            })
        },
        get_assinged_routes: function (schedule_id){
            var self = this;
            self.show_btn_add = false
            self.show_checkbox = false
            self.show_btn_remove = false
            self.selected_schedule = schedule_id;
    
            axios.get('/garage/api/schedule/get_assinged_routes/'+schedule_id+'/').then(function (response){
                self.title = 'Assinged route | Schedule ID '+schedule_id
                self.route_list = response.data
            })
        },
        unassing_route: function (schedule_id){
            var self = this;
            self.show_btn_add = false
            self.show_btn_remove = true
            self.show_checkbox = true
            self.selected_schedule = schedule_id;
    
            axios.get('/garage/api/schedule/unassing_route/'+schedule_id+'/').then(function (response){
                self.title = 'Unassing route | Schedule ID '+schedule_id
                self.route_list = response.data
            })
        },
        add_route: function (){
            var self = this;
            var data = {
                'schedule': self.selected_schedule,
                'selected_route': self.selected_route
            }
            axios.post('/garage/api/schedule/add/route/', data).then(function (response){
                self.selected_route = []
                self.get_assinged_routes(self.selected_schedule)
            })
            
        },
        remove_route: function (){
            var self = this;
            var data = {
                'schedule': self.selected_schedule,
                'selected_route': self.selected_route
            }
            axios.post('/garage/api/schedule/remove/route/', data).then(function (response){
                self.selected_route = []
                self.get_assinged_routes(self.selected_schedule)
            })
        }
    },
    beforeMount(){
        this.get_schedule_list()
     },
});