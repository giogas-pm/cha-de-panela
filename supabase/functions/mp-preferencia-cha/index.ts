// Kit do Chá — cria a preferência de pagamento (R$24,90) no Mercado Pago e devolve o link do checkout.
// Mesma receita da Carta do Noel. Nenhum dado da noiva passa por aqui: só o código aleatório do pedido.
const REF = "diemqzngskmcuytkzjhr";
const WEBHOOK_URL = `https://${REF}.supabase.co/functions/v1/mp-webhook-cha`;
const SITE = "https://giogas-pm.github.io/cha-de-panela/";
const PRECO = 24.9;
const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
function json(obj: unknown) {
  return new Response(JSON.stringify(obj), { headers: { ...CORS, "Content-Type": "application/json" } });
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  try {
    const token = Deno.env.get("MP_ACCESS_TOKEN");
    if (!token) return json({ ok: false, motivo: "sem_token" });
    const { slug } = await req.json().catch(() => ({} as any));
    if (!slug || !/^[a-z0-9]{6,20}$/.test(String(slug))) return json({ ok: false, motivo: "sem_slug" });
    const pref = {
      items: [{ title: "Kit de brincadeiras do chá personalizado", quantity: 1, unit_price: PRECO, currency_id: "BRL" }],
      external_reference: String(slug),
      metadata: { slug: String(slug), tipo: "kit_cha" },
      statement_descriptor: "KITDOCHA",
      notification_url: WEBHOOK_URL,
      back_urls: {
        success: `${SITE}?pago=ok#p=${slug}`,
        pending: `${SITE}?pago=pendente#p=${slug}`,
        failure: `${SITE}?pago=falhou#p=${slug}`,
      },
      auto_return: "approved",
    };
    const r = await fetch("https://api.mercadopago.com/checkout/preferences", {
      method: "POST",
      headers: { "Content-Type": "application/json", Authorization: "Bearer " + token },
      body: JSON.stringify(pref),
    });
    const j = await r.json();
    if (j && j.init_point) return json({ ok: true, init_point: j.init_point });
    return json({ ok: false, motivo: "mp_erro", detalhe: (j && (j.message || j.error)) || null });
  } catch (e) {
    return json({ ok: false, motivo: "excecao", detalhe: String(e) });
  }
});
