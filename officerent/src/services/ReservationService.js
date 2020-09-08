import axiosInstance from '../config/axios.config';

export default class ReservationService {
    // add method. once the endpoint is active, the method will be creating the record  
    async add(data) {
        try{
            const response = await axiosInstance.post('/reservation', data);
            return response.data;
        }
        catch(error){
            throw error.data;
        }
    }

    // delete method. once the endpoint is active, the method will be deleting the record of given id parameter
    async delete(id) {
      try{
          const response = await axiosInstance.delete('/reservation/' + id);
          return response.data;
      }
      catch(error){
          throw error.data;
      }
  }
}