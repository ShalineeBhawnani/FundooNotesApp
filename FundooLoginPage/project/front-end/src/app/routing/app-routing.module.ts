import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Route, RouterModule } from '@angular/router';
import { LoginComponent } from '../components/login/login.component';
import { RegisterComponent } from '../components/register/register.component';
import { ForgotpasswordComponent } from '../components/forgotpassword/forgotpassword.component';
import { ResetpasswordComponent } from '../components/resetpassword/resetpassword.component';
import { MyNavComponent } from '../components/my-nav/my-nav.component';
import { AuthGuard } from '../auth_guard/auth.guard'
import { LabelComponent } from '../components/label/label.component';
import { NoteComponent } from '../components/note/note.component';
import { NotedataComponent } from '../components/notedata/notedata.component';
import { ArchiveComponent}  from '../components/archive/archive.component';
import { TrashComponent } from '../components/trash/trash.component';



const routes: Route[] = [
  {path:'', redirectTo: '/login', pathMatch:'full'},
  {path:'login', component: LoginComponent},
  {path:'register', component:RegisterComponent},
  {path:'forgotpassword', component:ForgotpasswordComponent},
  {
    path:'resetpassword/:name',
    component: ResetpasswordComponent,
  },
  {path:'nav',
  component:MyNavComponent,

    children:[
      {path:'', redirectTo: 'note', pathMatch:'full'},
      {path:'note',
      component:NotedataComponent,
      canActivate: [AuthGuard]},
      {
        path:'reminder',
        component: NoteComponent
      },

    ]
},

{
  path:'label',
  component: LabelComponent,
  canActivate: [AuthGuard],

},



  {
    path:'trash',
    component: TrashComponent
  },

  {
    path:'archive',
    component: ArchiveComponent
  },


];

@NgModule({
  imports: [CommonModule,RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule { }
