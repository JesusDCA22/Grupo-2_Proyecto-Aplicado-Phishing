#### librerias ####
from tensorflow import keras

# --------------------------------------------------
# Evaluación final comparativa
# --------------------------------------------------
print("\n🔍 Resultados Finales:")
results = []
for name, model in best_models.items():
    loss, acc, auc, recall = model.evaluate(X_test, y_te_ohe, verbose=0)
    results.append({
        'Modelo': name,
        'Test Loss': f"{loss:.4f}",
        'Test Accuracy': f"{acc:.4f}",
        'Test AUC': f"{auc:.4f}",
        'Test Recall': f"{recall:.4f}"
    })

# Mostrar tabla comparativa
print(pd.DataFrame(results).sort_values('Test AUC', ascending=False))



best_model1 = keras.models.load_model('mejor_modelo_acc.keras')
best_model2 = keras.models.load_model('mejor_modelo_auc.keras')
best_model3 = keras.models.load_model('mejor_modelo_recall.keras')

# --------------------------------------------------
# Mejor Modelo AUC
# --------------------------------------------------

#final_model = best_model
final_model = best_model2

# Predicciones en el test set
y_pred_proba = final_model.predict(X_test)
y_pred = y_pred_proba.argmax(axis=1)

# Convertir one-hot encoding a labels
y_test_labels = y_te_ohe.argmax(axis=1)

# 1. Classification Report
print("Classification Report:")
print(classification_report(y_test_labels, y_pred, target_names=['legitimate', 'phishing']))
# 2. Matriz de Confusión
cm = confusion_matrix(y_test_labels, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['legitimate', 'phishing'],
            yticklabels=['legitimate', 'phishing'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
# 3. Métricas Adicionales
test_loss, test_acc, test_auc, test_recall = final_model.evaluate(X_test, y_te_ohe, verbose=0)

print("\nMétricas Finales:")
print(f"- Accuracy: {test_acc:.4f}")
print(f"- AUC: {test_auc:.4f}")
print(f"- Recall: {test_recall:.4f}")

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# 1. Obtener las probabilidades predichas para la clase positiva (phishing)
y_pred_proba = final_model.predict(X_test)[:, 1]  # Probabilidades de la clase 1 (phishing)

# 2. Calcular FPR, TPR y umbrales
fpr, tpr, thresholds = roc_curve(y_test_labels, y_pred_proba)

# 3. Calcular el AUC (Area Under the Curve)
roc_auc = auc(fpr, tpr)

# 4. Graficar la curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random guess (AUC = 0.50)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Curva ROC - Modelo de Detección de Phishing')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()


# --------------------------------------------------
# Mejor Modelo ACC
# --------------------------------------------------
final_model = best_model1

# Predicciones en el test set
y_pred_proba = final_model.predict(X_test)
y_pred = y_pred_proba.argmax(axis=1)

# Convertir one-hot encoding a labels
y_test_labels = y_te_ohe.argmax(axis=1)

# 1. Classification Report
print("Classification Report:")
print(classification_report(y_test_labels, y_pred, target_names=['legitimate', 'phishing']))
# 2. Matriz de Confusión
cm = confusion_matrix(y_test_labels, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['legitimate', 'phishing'],
            yticklabels=['legitimate', 'phishing'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
# 3. Métricas Adicionales
test_loss, test_acc, test_auc, test_recall = final_model.evaluate(X_test, y_te_ohe, verbose=0)

print("\nMétricas Finales:")
print(f"- Accuracy: {test_acc:.4f}")
print(f"- AUC: {test_auc:.4f}")
print(f"- Recall: {test_recall:.4f}")

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# 1. Obtener las probabilidades predichas para la clase positiva (phishing)
y_pred_proba = final_model.predict(X_test)[:, 1]  # Probabilidades de la clase 1 (phishing)

# 2. Calcular FPR, TPR y umbrales
fpr, tpr, thresholds = roc_curve(y_test_labels, y_pred_proba)

# 3. Calcular el AUC (Area Under the Curve)
roc_auc = auc(fpr, tpr)

# 4. Graficar la curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random guess (AUC = 0.50)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Curva ROC - Modelo de Detección de Phishing')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()

# --------------------------------------------------
# Mejor Modelo Recall
# --------------------------------------------------
final_model = best_model3

# Predicciones en el test set
y_pred_proba = final_model.predict(X_test)
y_pred = y_pred_proba.argmax(axis=1)

# Convertir one-hot encoding a labels
y_test_labels = y_te_ohe.argmax(axis=1)

# 1. Classification Report
print("Classification Report:")
print(classification_report(y_test_labels, y_pred, target_names=['legitimate', 'phishing']))
# 2. Matriz de Confusión
cm = confusion_matrix(y_test_labels, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=['legitimate', 'phishing'],
            yticklabels=['legitimate', 'phishing'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()
# 3. Métricas Adicionales
test_loss, test_acc, test_auc, test_recall = final_model.evaluate(X_test, y_te_ohe, verbose=0)

print("\nMétricas Finales:")
print(f"- Accuracy: {test_acc:.4f}")
print(f"- AUC: {test_auc:.4f}")
print(f"- Recall: {test_recall:.4f}")

from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# 1. Obtener las probabilidades predichas para la clase positiva (phishing)
y_pred_proba = final_model.predict(X_test)[:, 1]  # Probabilidades de la clase 1 (phishing)

# 2. Calcular FPR, TPR y umbrales
fpr, tpr, thresholds = roc_curve(y_test_labels, y_pred_proba)

# 3. Calcular el AUC (Area Under the Curve)
roc_auc = auc(fpr, tpr)

# 4. Graficar la curva ROC
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random guess (AUC = 0.50)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('Curva ROC - Modelo de Detección de Phishing')
plt.legend(loc="lower right")
plt.grid(True)
plt.show()
