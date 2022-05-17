new Vue({
    el:'#app',
    delimiters: ['{$', '$}'],
    data: {
        chauffeur_list:[]      
    },
    methods:{
        get_chauffeur_list: function (){
            var self = this;

            axios.get('/garage/api/chauffeur/list').then(function (response){
                self.chauffeur_list = response.data
            })
        }
    },
    beforeMount(){
        this.get_chauffeur_list()
     },
});