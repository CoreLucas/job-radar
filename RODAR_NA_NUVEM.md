# ☁️ Como Rodar o JobRadar na Nuvem (GitHub Actions)

## 🎯 O que você vai conseguir

- ✅ O programa roda **automaticamente a cada 3 horas**
- ✅ **24 horas por dia, 7 dias por semana**
- ✅ Totalmente **gratuito** (GitHub Actions é grátis para repositórios públicos)
- ✅ Não precisa deixar seu computador ligado
- ✅ Recebe notificações no Telegram mesmo com o PC desligado

---

## 📋 Pré-requisitos

- [x] Conta no GitHub (gratuita)
- [x] Bot do Telegram configurado (você já tem!)
- [x] Projeto JobRadar clonado localmente

---

## 🚀 Passo a Passo Completo

### **1. Criar Repositório no GitHub**

#### Opção A: Criar novo repositório
1. Acesse https://github.com/new
2. Nome do repositório: `job-radar` (ou o nome que quiser)
3. Escolha **Público** (para usar GitHub Actions grátis)
4. **NÃO** marque "Add a README file"
5. Clique em **Create repository**

#### Opção B: Fazer fork do repositório original
1. Acesse https://github.com/liliamkezia-star/job-radar
2. Clique em **Fork** no canto superior direito
3. Confirme a criação do fork na sua conta

---

### **2. Subir seu Código para o GitHub**

Abra o terminal na pasta do projeto:

```bash
cd c:\Users\lucas\Documents\jobradar\job-radar
```

#### Se criou repositório novo (Opção A):
```bash
# Inicializar git (se ainda não estiver inicializado)
git init

# Adicionar todos os arquivos
git add .

# Fazer o primeiro commit
git commit -m "Initial commit - JobRadar configurado"

# Conectar ao seu repositório (SUBSTITUA seu-usuario pelo seu usuário do GitHub)
git remote add origin https://github.com/seu-usuario/job-radar.git

# Renomear branch para main (se necessário)
git branch -M main

# Enviar para o GitHub
git push -u origin main
```

#### Se fez fork (Opção B):
```bash
# Adicionar o remote do seu fork (SUBSTITUA seu-usuario)
git remote set-url origin https://github.com/seu-usuario/job-radar.git

# Fazer commit das suas alterações
git add .
git commit -m "Personalização do JobRadar"

# Enviar para o seu fork
git push origin main
```

---

### **3. Configurar Secrets no GitHub** ⚠️ **IMPORTANTE!**

Os secrets guardam suas credenciais de forma segura (não ficam visíveis no código).

1. Acesse seu repositório no GitHub
2. Clique em **Settings** (Configurações)
3. No menu lateral, clique em **Secrets and variables** → **Actions**
4. Clique em **New repository secret**

#### Adicione 2 secrets:

**Secret 1: TELEGRAM_BOT_TOKEN**
- Name: `TELEGRAM_BOT_TOKEN`
- Secret: `8628737336:AAH5YgD5CEu64UeUTEPgNGxQnPUkoBNNKNs`
- Clique em **Add secret**

**Secret 2: TELEGRAM_CHAT_ID**
- Clique novamente em **New repository secret**
- Name: `TELEGRAM_CHAT_ID`
- Secret: `6365466199`
- Clique em **Add secret**

---

### **4. Ativar GitHub Actions**

1. No seu repositório, clique na aba **Actions**
2. Se aparecer um botão verde **"I understand my workflows, go ahead and enable them"**, clique nele
3. Pronto! O workflow está ativo

---

### **5. Testar o Workflow Manualmente**

Antes de esperar 3 horas, teste se está funcionando:

1. Vá na aba **Actions**
2. Clique no workflow **JobRadar** (lado esquerdo)
3. Clique no botão **Run workflow** (lado direito)
4. Clique em **Run workflow** (verde)
5. Aguarde alguns minutos
6. A execução vai aparecer na lista
7. Clique nela para ver os logs em tempo real
8. **Verifique seu Telegram!** Você deve receber notificações de vagas

---

## ⏰ Como Funciona a Automação

### Quando o programa roda automaticamente:

O arquivo `.github/workflows/jobradar.yml` está configurado com:

```yaml
schedule:
  - cron: "0 */3 * * *"
```

Isso significa:
- ✅ A cada **3 horas**
- ✅ Todos os dias
- ✅ Automaticamente

### Horários (UTC):
- 00:00 UTC = 21:00 (Brasil)
- 03:00 UTC = 00:00 (Brasil)
- 06:00 UTC = 03:00 (Brasil)
- 09:00 UTC = 06:00 (Brasil)
- 12:00 UTC = 09:00 (Brasil)
- 15:00 UTC = 12:00 (Brasil)
- 18:00 UTC = 15:00 (Brasil)
- 21:00 UTC = 18:00 (Brasil)

---

## 🔧 Personalizações

### Mudar o intervalo de execução

Edite o arquivo `.github/workflows/jobradar.yml`:

```yaml
schedule:
  - cron: "0 */1 * * *"  # A cada 1 hora
  - cron: "0 */2 * * *"  # A cada 2 horas
  - cron: "0 */6 * * *"  # A cada 6 horas
  - cron: "0 8,12,18 * * *"  # Às 8h, 12h e 18h (UTC)
```

Depois de editar:
```bash
git add .github/workflows/jobradar.yml
git commit -m "Ajusta intervalo de execução"
git push
```

### Desativar temporariamente

Se quiser pausar as buscas:

1. Vá em **Actions** no GitHub
2. Clique em **JobRadar** (workflow)
3. Clique nos três pontinhos **...** no canto superior direito
4. Clique em **Disable workflow**

Para reativar, repita os passos e clique em **Enable workflow**.

---

## 📊 Monitorar as Execuções

### Ver histórico de execuções:
1. Acesse a aba **Actions** no seu repositório
2. Veja todas as execuções passadas
3. Clique em qualquer uma para ver detalhes e logs

### Ver vagas encontradas:
- As vagas ficam salvas em `data/jobs.db`
- A cada execução, o bot faz commit automático desse arquivo
- Veja o histórico em **Commits** no GitHub

---

## ⚠️ Problemas Comuns

### ❌ "Workflow not found"
**Solução:** Certifique-se de que enviou os arquivos da pasta `.github/workflows/` para o GitHub

### ❌ "Error: TELEGRAM_BOT_TOKEN not found"
**Solução:** Verifique se configurou os Secrets corretamente no passo 3

### ❌ O workflow não executa automaticamente
**Solução:** 
- Repositórios novos podem levar até 1 hora para a primeira execução
- Execute manualmente uma vez (passo 5)
- Certifique-se que o workflow está **habilitado** em Actions

### ❌ "Permission denied" ao fazer push
**Solução:**
```bash
# Configure suas credenciais do GitHub
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"

# Use token de acesso pessoal em vez de senha
# Crie em: https://github.com/settings/tokens
```

---

## 🎁 Vantagens de Rodar na Nuvem

✅ **Gratuito:** GitHub Actions oferece 2.000 minutos grátis por mês  
✅ **Sempre ativo:** Roda mesmo com seu computador desligado  
✅ **Confiável:** Infraestrutura do GitHub  
✅ **Logs completos:** Veja exatamente o que aconteceu em cada execução  
✅ **Histórico versionado:** Todas as vagas encontradas ficam no Git  
✅ **Fácil de pausar:** Desative quando quiser sem deletar nada

---

## 📱 Resultados no Telegram

Você vai receber:
- 🚨 **Notificações imediatas** para vagas de alta relevância
- 📊 **Digest diário** com resumo das vagas encontradas
- 💓 **Heartbeat diário** confirmando que o robô está funcionando
- ⚠️ **Alertas** se alguma fonte de vagas parar de funcionar

---

## 🔐 Segurança

- ✅ Suas credenciais ficam em **Secrets** (criptografadas)
- ✅ Nunca aparecem nos logs públicos
- ✅ Apenas você tem acesso aos Secrets
- ⚠️ **NUNCA** faça commit do arquivo `.env` com suas credenciais!

---

## 💡 Dica Final

Depois de configurar:
1. Faça um **teste manual** (passo 5)
2. Aguarde 3 horas para ver a primeira execução automática
3. Acompanhe pelo Telegram e pela aba Actions
4. Personalize os termos de busca em `core/config.py` conforme necessário

---

**Pronto! Seu JobRadar agora roda na nuvem 24/7! 🚀**
