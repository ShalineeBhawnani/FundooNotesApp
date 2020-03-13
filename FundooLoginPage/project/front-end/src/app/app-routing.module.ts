import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Route, RouterModule } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { ForgotpasswordComponent } from './forgotpassword/forgotpassword.component';
import { ResetpasswordComponent } from './resetpassword/resetpassword.component';
import { MyNavComponent } from './my-nav/my-nav.component';
import { AuthGuard } from './auth.guard'
import { LabelComponent } from './label/label.component';
import { NoteComponent } from './note/note.component';


const routes: Route[] = [
  {path:'', redirectTo: '/login', pathMatch:'full'},
  {path:'login', component: LoginComponent},
  {path:'register', component:RegisterComponent},
  {path:'forgotpassword', component:ForgotpasswordComponent},
  {
    path:'resetpassword/:name',
    component: ResetpasswordComponent,
  },

  { path:'nav',
    component:MyNavComponent,
    canActivate: [AuthGuard]
},
  {
    path:'label',
    component: LabelComponent,
    canActivate: [AuthGuard]
  },
  {
    path:'note',
    component: NoteComponent

  },
  {
    path:'reminder',
    component: NoteComponent
  },
  {
    path:'archive',
    component: NoteComponent
  },
  {
    path:'bin',
    component: NoteComponent
  },
];

@NgModule({
  imports: [CommonModule,RouterModule.forRoot(routes)],
  exports: [RouterModule],
  declarations: []
})
export class AppRoutingModule { }
