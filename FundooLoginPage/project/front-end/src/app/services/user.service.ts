import { Injectable } from '@angular/core';
import { HttpClient,HttpResponse,HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

import { environment } from '../../environments/environment';



@Injectable()
export class UserService {

  baseUrl = environment.baseUrl;
  httpHeaders = new HttpHeaders({'Content-type': 'application/json'})

  constructor(private http: HttpClient) { }

  login(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/login/',userData,{
      responseType: 'text',
    });

  }

  register(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/registration/',userData,{
      responseType: 'text',
    });

  }

  forgotuser(userData): Observable<any>
  {
    return this.http.post(this.baseUrl+'/forgotpassword/',userData,{
      responseType: 'text',
    });

  }

  resetuser(userData,username): Observable<any>

  {
    return this.http.post(this.baseUrl+'/resetpassword/'+username,userData,{
      responseType: 'text',
    });

  }

  label(noteData):Observable<any>
{

      console.log(localStorage.getItem('token'))
      return this.http.post(this.baseUrl+'/label/', noteData, { headers: {
        'token': localStorage.getItem('token')
      } });
    }

  
createNote(userData):Observable<any>
  {

        console.log(localStorage.getItem('token'))
        return this.http.post(this.baseUrl+'/note/', userData, { headers: {
          'token': localStorage.getItem('token')
        } });
      }

getAllNote():Observable<any>
{
  return this.http.get(this.baseUrl+'/note/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

updateAllNote():Observable<any>
{
  return this.http.get(this.baseUrl+'/updatenote/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}
ArchiveNote():Observable<any>
{
  return this.http.get(this.baseUrl+'/archive/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

bin():Observable<any>
{
  return this.http.get(this.baseUrl+'/bin/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

updateNotes(userData,note_id):Observable<any>
{
return this.http.put(this.baseUrl+'/noteupdate/'+note_id,userData,{headers:{
'token':localStorage.getItem('token')}}
);
}

updateLabel(data):Observable<any>
{
return this.http.put(this.baseUrl+'/labelupdate/',data,{headers:{
'token':localStorage.getItem('token')}}
);
}
deleteLabel(data):Observable<any>
{
  return this.http.put(this.baseUrl+'/labelupdate/',data,
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

getAllLabel():Observable<any>
{
  return this.http.get(this.baseUrl+'/label/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

uploadProfileImage(formData):Observable<any>
{
  return this.http.post(this.baseUrl+'/profile/',formData,
  { headers: {
    'token': localStorage.getItem('token')
  } });
}
getProfilemage():Observable<any>
{
  return this.http.get(this.baseUrl+'/profile/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

searchNote():Observable<any>
{
  return this.http.get(this.baseUrl+'/search/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}
getReminder():Observable<any>
{
  return this.http.get(this.baseUrl+'/reminder/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}
addCollaborator():Observable<any>
{
  return this.http.get(this.baseUrl+'/note/',
  { headers: {
    'token': localStorage.getItem('token')
  } });
}

}
