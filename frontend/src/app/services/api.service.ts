import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://127.0.0.1:8000/api';  // L'URL de ton backend Django

  constructor(private http: HttpClient) { }

  // Exemple de méthode pour récupérer la liste des produits
  getProducts(): Observable<any> {
    return this.http.get(`${this.apiUrl}/products/`);
  }
}
