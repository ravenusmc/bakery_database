import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import store from '@/store/index';

Vue.use(Vuex);

const data = {
	actionFound: false,
};

const getters = {
	actionFound: (state) => state.actionFound,
};

const actions = {


	submitDaySalesToDataBase: ({ commit }, { payload }) => {
		const path = 'http://localhost:5000/submitSalesDataToDatabase';
		axios.post(path, payload)
			.then((res) => {
				commit('setActionFound', false);
			})
			.catch((error) => {
				console.log(error);
			});
	},


};

const mutations = {

	setActionFound(state, value) {
		state.actionFound = value;
	},

};

export default {
	namespaced: true,
	state: data,
	getters,
	actions,
	mutations,
};