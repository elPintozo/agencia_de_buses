new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        selected_chauffeur:'',
        selected_route:[],
        route_list:[],
        chauffeur_list:[],
        title:'',
        show_btn_add: false,
        show_btn_remove: false,
        show_checkbox:false,
        new_dni_for_chauffeur:'',
    },
    methods:{
        get_chauffeur_list: function (){
            var self = this;

            axios.get('/garage/api/chauffeur/list').then(function (response){
                self.chauffeur_list = response.data
            })
        },
        assing_route: function (chauffeur_id){
            var self = this;
            self.show_btn_add = true
            self.show_checkbox = true
            self.show_btn_remove = false
            self.selected_chauffeur = chauffeur_id;
    
            axios.get('/garage/api/chauffeur/assing_route/'+chauffeur_id+'/').then(function (response){
                self.title = 'Assing route | Chauffeur ID '+chauffeur_id
                self.route_list = response.data
            })
        },
        get_assinged_routes: function (chauffeur_id){
            var self = this;
            self.show_btn_add = false
            self.show_checkbox = false
            self.show_btn_remove = false
            self.selected_chauffeur = chauffeur_id;
    
            axios.get('/garage/api/chauffeur/get_assinged_routes/'+chauffeur_id+'/').then(function (response){
                self.title = 'Assinged route | Chauffeur ID '+chauffeur_id
                self.route_list = response.data
            })
        },
        unassing_route: function (chauffeur_id){
            var self = this;
            self.show_btn_add = false
            self.show_btn_remove = true
            self.show_checkbox = true
            self.selected_chauffeur = chauffeur_id;
    
            axios.get('/garage/api/chauffeur/unassing_route/'+chauffeur_id+'/').then(function (response){
                self.title = 'Unassing route | Chauffeur ID '+chauffeur_id
                self.route_list = response.data
            })
        },
        add_route: function (){
            var self = this;
            var data = {
                'chauffeur': self.selected_chauffeur,
                'selected_route': self.selected_route
            }
            axios.post('/garage/api/chauffeur/add/route/', data).then(function (response){
                self.selected_route = []
                self.get_assinged_routes(self.selected_chauffeur)
            })
            
        },
        remove_route: function (){
            var self = this;
            var data = {
                'chauffeur': self.selected_chauffeur,
                'selected_route': self.selected_route
            }
            axios.post('/garage/api/chauffeur/remove/route/', data).then(function (response){
                self.selected_route = []
                self.get_assinged_routes(self.selected_chauffeur)
            })
        },
        btn_add_new_chauffeur: function (){
            var self = this;
            var data = {
                'dni': self.new_dni_for_chauffeur,
            }
            axios.post('/garage/api/chauffeur/list', data).then(function (response){
                self.new_dni_for_chauffeur = ''
                self.get_chauffeur_list()
            })
        },
    },
    beforeMount(){
        this.get_chauffeur_list()
     },
});